from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.core.paginator import Paginator
from recipe.models import Recipe, Like, Comment, Favourite
from recipe.forms import CommentForm
from .models import Profile
from .forms import ProfileForm


@login_required
def dashboard(request, filter_type=None):
    user = request.user

    ALLOWED_FILTERS = {"my", "favourites", None}
    if filter_type not in ALLOWED_FILTERS:
        return HttpResponseBadRequest("Invalid filter type.")

    # Recipes
    if filter_type == "my":
        queryset = Recipe.objects.filter(author=user)
    elif filter_type == "favourites":
        queryset = Recipe.objects.filter(favourited_by__user=user).distinct()
    else:
        queryset = Recipe.objects.all()

    paginate_by = Paginator(queryset, 8)
    page_number = request.GET.get("page")
    recipes = paginate_by.get_page(page_number)

    for recipe in recipes:
        recipe.is_liked = Like.objects.filter(
            user=request.user, recipe=recipe).exists()
        recipe.like_count = recipe.liked_by.count()
        recipe.comment_count = recipe.comments.all().count()
        recipe.is_favourite = Favourite.objects.filter(
            user=request.user, recipe=recipe).exists()

    # Profile
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)
        messages.info(request, "New profile was created for your account.")

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('dashboard')
    else:
        profile_form = ProfileForm(instance=profile)

    profile_image_url = profile.image.url if profile.image else None
    show_default_image = "placeholder" in profile_image_url if profile_image_url else True

    context = {
        "recipes": recipes,
        "filter_type": filter_type,
        "profile_form": profile_form,
        "profile": profile,
        "profile_image_url": profile_image_url,
        "show_default_image": show_default_image,
    }

    return render(
        request,
        "user_profile/dashboard.html",
        context,
    )


@login_required
def recipe_detail(request, pk):
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, id=pk)

    comments = recipe.comments.all().order_by("-updated_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request, "Comment successfully submitted.")

    comment_form = CommentForm()

    context = {
        "recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }

    return render(
        request,
        "user_profile/recipe_detail.html",
        context,
    )


@login_required
def recipe_like(request, pk):
    user = request.user
    recipe = get_object_or_404(Recipe, id=pk)

    # add record to Like model
    try:
        Like.objects.create(user=user, recipe=recipe)
        messages.success(request, f"You liked {recipe.title}!")
    except IntegrityError:
        messages.warning(request, f"You've already liked {recipe.title}!")
        pass

    # Redirect back to the page the user came from, if exists,
    # else to dashboard
    referer = request.META.get("HTTP_REFERER")
    if referer:
        return redirect(referer)
    else:
        return redirect("dashboard")


@login_required
def recipe_unlike(request, pk):
    user = request.user
    recipe = get_object_or_404(Recipe, id=pk)
    like = get_object_or_404(Like, user=user, recipe=recipe)
    like.delete()
    messages.error(request, f"You no longer like {recipe.title}!")

    referer = request.META.get("HTTP_REFERER")
    if referer:
        return redirect(referer)
    else:
        return redirect("dashboard")


@login_required
def comment_edit(request, recipe_id, comment_id):
    if request.method != "POST":
        messages.warning(request, "Invalid request method.")
        return redirect("recipe_detail", recipe_id)

    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=recipe_id)
        comment = get_object_or_404(Comment, id=comment_id)
        comment_form = CommentForm(request.POST, instance=comment)

        if comment.author != request.user:
            messages.error(request, "You are not allowed to edit this comment.")
            return redirect("recipe_detail", recipe_id)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment successfully updated.")
        else:
            messages.error(request, "Error updating comment. Please try again.")

    return HttpResponseRedirect(reverse('recipe_detail', args=[recipe_id]))


@login_required
def comment_delete(request, recipe_id, comment_id):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment successfully deleted!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return redirect("recipe_detail", recipe_id)


@login_required
def add_to_favourites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if Favourite.objects.filter(user=request.user, recipe=recipe).exists():
        messages.info(request, "This recipe is already in your favourites.")
    else:
        Favourite.objects.create(user=request.user, recipe=recipe)
        messages.success(request, "Recipe successfully added to favourites.")

    return redirect("dashboard")


@login_required
def remove_from_favourites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favourite = Favourite.objects.filter(
        user=request.user, recipe=recipe).first()

    if favourite:
        favourite.delete()
        messages.error(request, "Recipe removed from favourites.")
    else:
        messages.info(request, "This recipe was not in your favourites.")

    referer = request.META.get("HTTP_REFERER")
    if referer:
        return redirect(referer)
    else:
        return redirect("dashboard")
