# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| home | [home.html](https://github.com/marijavelickovska/grow_healthy/blob/main/home/templates/home/home.html) | ![screenshot](documentation/validation/html-home-home.png) |  |
| user_profile | [dashboard.html](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/templates/user_profile/dashboard.html) | ![screenshot](documentation/validation/html-user_profile-dashboard.png) |  |
| user_profile | [recipe_detail.html](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/templates/user_profile/recipe_detail.html) | ![screenshot](documentation/validation/html-user_profile-recipe_detail.png) | During testing, 6 errors and 1 warning appear on recipe_detail.html, but these issues do not originate directly from this page. The reason is that recipe_detail.html extends ({% extends 'dashboard.html' %}), and dashboard.html passes without errors when tested separately. |
| user_profile | [add_recipe.html](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/templates/user_profile/add_recipe.html) | ![screenshot](documentation/validation/html-user_profile-add_recipe.png) | During testing, 4 errors appear on add_recipe.html, but these errors do not originate directly from this page. The reason is that add_recipe.html extends ({% extends 'dashboard.html' %}), and dashboard.html passes without errors when tested separately. |
| templates | [404.html](https://github.com/marijavelickovska/grow_healthy/blob/main/templates/404.html) | ![screenshot](documentation/validation/html-templates-404.png) | |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot |  Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/marijavelickovska/grow_healthy/blob/main/static/css/style.css) | [link](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](documentation/validation/css-static-style.png) | |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [script.js](https://github.com/marijavelickovska/grow_healthy/blob/main/static/js/script.js) | N/A | ![screenshot](documentation/validation/js-static-script.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| grow_healthy | [settings.py](https://github.com/marijavelickovska/grow_healthy/blob/main/grow_healthy/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/grow_healthy/settings.py) | ![screenshot](documentation/validation/py-grow_healthy-settings.png) | |
| grow_healthy | [urls.py](https://github.com/marijavelickovska/grow_healthy/blob/main/grow_healthy/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/grow_healthy/urls.py) | ![screenshot](documentation/validation/py-grow_healthy-urls.png) | |
| home | [urls.py](https://github.com/marijavelickovska/grow_healthy/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) | |
| home | [views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) | |
| recipe | [test_forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/tests/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/recipe/tests/test_forms.py) | ![screenshot](documentation/validation/py-recipe-test-forms.png) | |
| recipe | [test_views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/tests/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/recipe/tests/test_views.py) | ![screenshot](documentation/validation/py-recipe-test-views.png) | |
| recipe | [admin.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/admin.py) | ![screenshot](documentation/validation/py-recipe-admin.png) | |
| recipe | [forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/forms.py) | ![screenshot](documentation/validation/py-recipe-forms.png) | |
| recipe | [models.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/models.py) | ![screenshot](documentation/validation/py-recipe-models.png) | |
| recipe | [views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/views.py) | ![screenshot](documentation/validation/py-recipe-views.png) | |
| user_profile | [test-forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/tests/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/user_profile/tests/test_forms.py) | ![screenshot](documentation/validation/py-user_profile-test-forms.png) | |
| user_profile | [test-views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/tests/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/user_profile/tests/test_views.py) | ![screenshot](documentation/validation/py-user_profile-test-views.png) | |
| user_profile | [admin.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/admin.py) | ![screenshot](documentation/validation/py-user_profile-admin.png) | |
| user_profile | [context_processors.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/context_processors.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/context_processors.py) | ![screenshot](documentation/validation/py-user_profile-context_processors.png) | |
| user_profile | [forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/forms.py) | ![screenshot](documentation/validation/py-user_profile-forms.png) | |
| user_profile | [models.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/models.py) | ![screenshot](documentation/validation/py-user_profile-models.png) | |
| user_profile | [urls.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/urls.py) | ![screenshot](documentation/validation/py-user_profile-urls.png) | |
| user_profile | [views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/views.py) | ![screenshot](documentation/validation/py-user_profile-views.png) | |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Signup | ![screenshot](documentation/responsiveness/mobile-signup.png) | ![screenshot](documentation/responsiveness/tablet-signup.png) | ![screenshot](documentation/responsiveness/desktop-signup.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Dashboard | ![screenshot](documentation/responsiveness/mobile-dashboard.png) | ![screenshot](documentation/responsiveness/tablet-dashboard.png) | ![screenshot](documentation/responsiveness/desktop-dashboard.png) | Works as expected |
| Recipe Detail | ![screenshot](documentation/responsiveness/mobile-recipe_detail.png) | ![screenshot](documentation/responsiveness/tablet-recipe_detail.png) | ![screenshot](documentation/responsiveness/desktop-recipe_detail.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/responsiveness/mobile-add_recipe.png) | ![screenshot](documentation/responsiveness/tablet-add_recipe.png) | ![screenshot](documentation/responsiveness/desktop-add_recipe.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Edge | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/edge-home.png) | Works as expected |
| Signup | ![screenshot](documentation/browsers/chrome-signup.png) | ![screenshot](documentation/browsers/firefox-signup.png) | ![screenshot](documentation/browsers/edge-signup.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/edge-login.png) | Works as expected |
| Dashboard | ![screenshot](documentation/browsers/chrome-dashboard.png) | ![screenshot](documentation/browsers/firefox-dashboard.png) | ![screenshot](documentation/browsers/edge-dashboard.png) | Works as expected |
| Recipe Detail | ![screenshot](documentation/browsers/chrome-recipe_detail.png) | ![screenshot](documentation/browsers/firefox-recipe_detail.png) | ![screenshot](documentation/browsers/edge-recipe_detail.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/browsers/chrome-add_recipe.png) | ![screenshot](documentation/browsers/firefox-add_recipe.png) | ![screenshot](documentation/browsers/edge-add_recipe.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/edge-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Signup | ![screenshot](documentation/lighthouse/mobile-signup.png) | ![screenshot](documentation/lighthouse/desktop-signup.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Dashboard | ![screenshot](documentation/lighthouse/mobile-dashboard.png) | ![screenshot](documentation/lighthouse/desktop-dashboard.png) |
| Recipe Detail | ![screenshot](documentation/lighthouse/mobile-recipe_detail.png) | ![screenshot](documentation/lighthouse/desktop-recipe_detail.png) |
| Add Recipe | ![screenshot](documentation/lighthouse/mobile-add_recipe.png) | ![screenshot](documentation/lighthouse/desktop-add_recipe.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Home | When a non-logged-in user clicks on a recipe, they should not be able to access the recipe details. Instead, they should be informed that they need to log in to view the recipe details. | Clicked on a recipe while not logged in. | The page scrolled down to the "Join us" section and displayed the message: "To see the recipe details, please log in or sign up." | ![screenshot](documentation/defensive/recipe-click-not-logged-in.png) |
| Dashboard | After successful login, the user should be redirected to the dashboard. Their profile name should appear in the navbar, and a success message should be displayed below the navbar. | Logged in with valid user credentials. | User was redirected to the dashboard. The navbar showed "Hello [username]", and a success message appeared below the navbar. | ![screenshot](documentation/defensive/login-success.png) |
| | When clicking the edit button, the disabled fields (name, about me, and profile picture) should become enabled for editing. After clicking save, the updated information should be saved successfully. | Clicked the edit button, modified the name, about me, and profile picture fields, then clicked save. | The fields were enabled after clicking edit, changes were saved successfully after clicking save. | ![screenshot](documentation/defensive/dashboard-edit-profile.png) |
| | If there are more than 8 recipes, pagination should appear. The correct number of pages should be shown. On the first page, only the "Next" button should be visible; on the last page, only the "Previous" button should be shown. | Added more than 8 recipes to the dashboard and navigated through pages. | Pagination appeared correctly. Page numbers were displayed. The first page showed only the "Next" button, and the last page showed only the "Previous" button. | ![screenshot](documentation/defensive/pagination.png) |
| | On clicking "My Recipes" in the sub-navbar, only the recipes added by the logged-in user should be displayed. | Clicked "My Recipes" in the sub-navbar. | Only the user's own recipes were displayed correctly. | ![screenshot](documentation/defensive/dashboard-my-recipes.png) |
| | On clicking "Favourites" in the sub-navbar, only the recipes marked as favourite by the user should be displayed. | Clicked "Favourites" in the sub-navbar. | Only the user's favourite recipes were displayed correctly. | ![screenshot](documentation/defensive/dashboard-favourites.png) |
| | Each recipe card should display icons for like, comment, and favourites. Clicking the like icon should increase the like count and highlight the icon; clicking again should undo the like. Clicking the comment icon should navigate to the recipe detail page with the comments section. Clicking the favourites icon should turn it red to indicate it is saved; clicking again should remove it from favourites and reset the icon color. After each action, the user should be notified with a success message. | Clicked like – icon highlighted and count increased; clicked again – count decreased and icon reset. Clicked comment – navigated to recipe detail with comments visible. Clicked favourites – icon turned red; clicked again – icon reset. After each click, a success message was displayed to confirm the action. | All three icons functioned correctly with appropriate actions, visual feedback, and success messages. | ![screenshot](documentation/defensive/recipe-card-icons.png) |
| Recipe Detail | When a logged-in user clicks on a recipe, the recipe details should open and display all necessary fields such as image, title, meal type, ingredients, instructions, creator, date, comments, a form to add comments, and edit/delete buttons for both the recipe and comments if they belong to the logged-in user. Otherwise, the edit/delete buttons should not be visible. | Logged in as a user and clicked on a recipe. Verified the display of all recipe details and the visibility of edit/delete buttons only on user-owned content. | Recipe details displayed correctly. Edit and delete buttons appeared only for the recipe and comments owned by the logged-in user. | ![screenshot](documentation/defensive/recipe-detail-logged-in.png) |
| | On clicking the edit icon, the edit recipe form should open. Upon submitting valid changes, the recipe should be successfully updated and a confirmation message should be displayed. | Clicked "Edit Recipe", modified title and ingredients, then submitted the form. | The recipe was successfully updated and a "Recipe successfully updated." message appeared. | ![screenshot](documentation/defensive/edit-recipe-success.png) |
| | On clicking the delete icon, a confirmation modal should appear. Upon clicking delete, the recipe should be successfully deleted and a success message should be displayed. | Clicked the delete icon, confirmed the deletion in the modal. | The recipe was successfully deleted and a "Receptot e uspesno izbrisan" message appeared. | ![screenshot](documentation/defensive/delete-recipe-success.png) |
| | Clicking on the author's name (next to "Created by" in the recipe section and in the comments) should open a modal showing the author's information including their profile picture, name, and about section. | Clicked the author's name in both the recipe and comment sections. | A modal appeared displaying the creator's profile image, full name, and about info. | ![screenshot](documentation/defensive/author-info-modal.png) |
| | Clicking the edit icon on a recipe should open the edit form populated with the recipe's existing data. After correctly filling in the form and submitting, the recipe should be updated and a success message should be displayed. | Clicked the edit icon – form opened with pre-filled data. Modified fields and submitted. | Recipe was successfully updated and a "Recipe successfully updated" message appeared. | ![screenshot](documentation/defensive/edit-recipe.png) |
| | If the logged-in user clicks the delete icon on one of their own recipes, the recipe should be deleted and a success message should be shown. | Clicked the delete icon on a recipe owned by the logged-in user. | Recipe was successfully deleted and a "Recipe was successfully deleted" message appeared. | ![screenshot](documentation/defensive/delete-recipe.png) |
| | Below the recipe details, there is a comments section displaying all existing comments and a form to add a new one. On submitting the form, a new comment should be successfully added. For comments authored by the currently logged-in user, edit and delete icons should appear. Clicking edit allows the comment to be updated; clicking delete removes the comment. After each action, a success message should be displayed. | Submitted a new comment – it appeared in the list. On an existing comment owned by the logged-in user, clicked edit – updated comment was saved and message shown. Clicked delete – comment was removed and confirmation message appeared. | Add, edit, and delete actions worked correctly with appropriate UI updates and success messages for each. | ![screenshot](documentation/defensive/comment-section.png) |
| Add Recipe | If the user tries to submit the add recipe form without filling in one or more required fields, the form should not submit and validation messages should be displayed indicating which fields are required. | Opened the add recipe page, left required fields empty, and clicked submit. | Form was not submitted. Validation messages appeared next to the empty required fields indicating they are mandatory. | ![screenshot](documentation/defensive/add-recipe-validation.png) |
| | On correctly filling all required fields and submitting the form, the recipe should be saved, displayed in "My Recipes", and a success message "Recipe added successfully" should be shown. | Filled in all required fields and submitted the form. | Recipe was added successfully, appeared in "My Recipes", and a success message was shown. | ![screenshot](documentation/defensive/add-recipe-success.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I can visit the homepage and immediately understand what the site is about and view recipes | so that I know what the platform offers and can explore content. | ![screenshot](documentation/features/home.png) |
| As a user | I can register and create a profile | so that I can save my preferences and post recipes. | ![screenshot](documentation/features/login.png) |
| As a user | I can add a new recipe | so that I can share my ideas with others. | ![screenshot](documentation/features/add_recipe.png) |
| As a user | I can view a recipe with ingredients and steps | so that I can follow it easily while cooking. | ![screenshot](documentation/features/recipe_detail.png) |
| As a user | I can favorite a recipe | so that I can easily find it later. | ![screenshot](documentation/features/dashboard-favourites.png) |
| As a user | I can like or unlike a recipe | so that I can show appreciation or remove my like. | ![screenshot](documentation/features/like_comment_favourite.png) |
| As a user | I can comment on recipes | so that I can give feedback or ask questions. | ![screenshot](documentation/features/add_comment.png) |
| As a user | I can see the number of likes and comments on each recipe | so that I know which recipes are popular. | ![screenshot](documentation/features/like_comment_favourite.png) |
| As a user | I can click on a recipe or comment author to view their profile information in a modal | so that I can learn more about the person who created the content. | ![screenshot](documentation/features/author-info-modal.png) |
| As a site admin | I can manage user comments and recipes | so that I can remove any inappropriate content. | ![screenshot](documentation/features/admin.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python manage.py test recipe.tests.test_forms`
- `python manage.py test recipe.tests.test_views`
- `python manage.py test user_profile.tests.test_forms`
- `python manage.py test user_profile.tests.test_views`

| App | Test | Screenshot |
| --- | --- | --- |
| recipe | forms | ![screenshot](documentation/automation/recipe-test-forms.png) |
| recipe | views | ![screenshot](documentation/automation/recipe-test-forms.png) |
| user_profile | forms | ![screenshot](documentation/automation/user_profile-test-forms.png) |
| user_profile | views | ![screenshot](documentation/automation/user_profile-test-forms.png) |


## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Amarijavelickovska%2Fgrow_healthy%20label%3Abug&label=bugs)](https://www.github.com/marijavelickovska/grow_healthy/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/marijavelickovska/grow_healthy/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/marijavelickovska/grow_healthy/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

[![GitHub issues](https://img.shields.io/github/issues/marijavelickovska/grow_healthy)](https://www.github.com/marijavelickovska/grow_healthy/issues)

Any remaining open issues can be tracked [here](https://www.github.com/marijavelickovska/grow_healthy/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| Errors that appeared during HTML validation of the recipe_detail.html. | ![screenshot](documentation/issues/html-user_profile-recipe_detail.png) |
| Errors that appeared during HTML validation of the add_recipe.html. | ![screenshot](documentation/issues/html-user_profile-add_recipe.png) |



> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

