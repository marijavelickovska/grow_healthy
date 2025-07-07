const editCommentButtons = document.getElementsByClassName("btn-edit-comment");
const commentText = document.getElementById("id_body"); 
const commentForm = document.getElementById("commentForm");
const submitCommentButton = document.getElementById("submitCommentButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteModalBody = document.getElementById("deleteModalBody");
const deleteModalTitle = document.getElementById("deleteModalTitle");

// On DOMContentLoaded: Add event listener to cards to show a message when clicked
document.addEventListener("DOMContentLoaded", function () {
   let cards = document.getElementsByClassName("card-home");

    for (let card of cards) {
        card.addEventListener("click", showRecipeMessage);
    }

});


// Scroll to the section where the message for login and register are displayed and set a timeout to hide it
function showRecipeMessage() {
    let messageDiv = document.getElementById("recipe-message");
    let joinSection = document.getElementById("join_us");
    messageDiv.style.display = "block";

    setTimeout(() => {
        messageDiv.style.display = "none";
    }, 5000);

    if (joinSection) {
        joinSection.scrollIntoView({
            behavior: "smooth"
        });
    }
}


for (let button of editCommentButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("data-comment_id");
    let recipeId = e.currentTarget.getAttribute("data-recipe_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitCommentButton.innerText = "Update";
    commentForm.setAttribute("action", `/user_profile/recipe/${recipeId}/edit_comment/${commentId}/`);

    // Scroll to the add_comment section
    const commentSection = document.getElementById("add_comment");
    if (commentSection) {
      commentSection.scrollIntoView({ behavior: "smooth" });
    }
  });
}


const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");
for (let button of deleteCommentButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("data-comment_id");
    let recipeId = e.currentTarget.getAttribute("data-recipe_id");
    
    deleteModalTitle.innerText = "Delete comment?";
    deleteModalBody.innerText = "Are you sure you want to delete your comment? This action cannot be undone.";
    deleteConfirm.href = `/user_profile/recipe/${recipeId}/delete_comment/${commentId}/`;
    
    deleteModal.show();
  });
}


const deleteRecipeButtons = document.getElementsByClassName("btn-delete-recipe");
for (let button of deleteRecipeButtons) {
  button.addEventListener("click", (e) => {
    let recipeId = e.currentTarget.getAttribute("data-recipe_id");

    deleteModalTitle.innerText = "Delete recipe?";
    deleteModalBody.innerText = "Are you sure you want to delete this recipe? This action cannot be undone.";
    deleteConfirm.href = `/user_profile/delete_recipe/${recipeId}/`;

    deleteModal.show();
  });
}


