# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| home | [home.html](https://github.com/marijavelickovska/grow_healthy/blob/main/home/templates/home/home.html) | ![screenshot](documentation/validation/html-home-home.png) | Notes (if applicable) |
| user_profile | [dashboard.html](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/templates/user_profile/dashboard.html) | ![screenshot](documentation/validation/html-user_profile-dashboard.png) | Notes (if applicable) |
| user_profile | [recipe_detail.html](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/templates/user_profile/recipe_detail.html) | ![screenshot](documentation/validation/html-user_profile-recipe_detail.png) | During testing, 6 errors and 1 warning appear on recipe_detail.html, but these issues do not originate directly from this page. The reason is that recipe_detail.html extends ({% extends 'dashboard.html' %}), and dashboard.html passes without errors when tested separately. |
| user_profile | [add_recipe.html](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/templates/user_profile/add_recipe.html) | ![screenshot](documentation/validation/html-user_profile-add_recipe.png) | During testing, 4 errors appear on add_recipe.html, but these errors do not originate directly from this page. The reason is that add_recipe.html extends ({% extends 'dashboard.html' %}), and dashboard.html passes without errors when tested separately. |
| templates | [404.html](https://github.com/marijavelickovska/grow_healthy/blob/main/templates/404.html) | ![screenshot](documentation/validation/html-templates-404.png) | Notes (if applicable) |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot |  Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/marijavelickovska/grow_healthy/blob/main/static/css/style.css) | [link](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](documentation/validation/css-static-style.png) | 


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [script.js](https://github.com/marijavelickovska/grow_healthy/blob/main/static/js/script.js) | N/A | ![screenshot](documentation/validation/js-static-script.png) |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| grow_healthy | [settings.py](https://github.com/marijavelickovska/grow_healthy/blob/main/grow_healthy/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/grow_healthy/settings.py) | ![screenshot](documentation/validation/py-grow_healthy-settings.png) | Notes (if applicable) |
| grow_healthy | [urls.py](https://github.com/marijavelickovska/grow_healthy/blob/main/grow_healthy/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/grow_healthy/urls.py) | ![screenshot](documentation/validation/py-grow_healthy-urls.png) | Notes (if applicable) |
| home | [urls.py](https://github.com/marijavelickovska/grow_healthy/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) | Notes (if applicable) |
| home | [views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) | Notes (if applicable) |
| recipe | [test_forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/tests/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/recipe/tests/test_forms.py) | ![screenshot](documentation/validation/py-recipe-test-forms.png) | Notes (if applicable) |
| recipe | [test_views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/tests/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/recipe/tests/test_views.py) | ![screenshot](documentation/validation/py-recipe-test-views.png) | Notes (if applicable) |
| recipe | [admin.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/admin.py) | ![screenshot](documentation/validation/py-recipe-admin.png) | Notes (if applicable) |
| recipe | [forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/forms.py) | ![screenshot](documentation/validation/py-recipe-forms.png) | Notes (if applicable) |
| recipe | [models.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/models.py) | ![screenshot](documentation/validation/py-recipe-models.png) | Notes (if applicable) |
| recipe | [views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/recipe/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/recipe/views.py) | ![screenshot](documentation/validation/py-recipe-views.png) | Notes (if applicable) |
| user_profile | [test-forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/tests/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/user_profile/tests/test_forms.py) | ![screenshot](documentation/validation/py-user_profile-test-forms.png) | Notes (if applicable) |
| user_profile | [test-views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/tests/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/refs/heads/main/user_profile/tests/test_views.py) | ![screenshot](documentation/validation/py-user_profile-test-views.png) | Notes (if applicable) |
| user_profile | [admin.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/admin.py) | ![screenshot](documentation/validation/py-user_profile-admin.png) | Notes (if applicable) |
| user_profile | [context_processors.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/context_processors.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/context_processors.py) | ![screenshot](documentation/validation/py-user_profile-context_processors.png) | Notes (if applicable) |
| user_profile | [forms.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/forms.py) | ![screenshot](documentation/validation/py-user_profile-forms.png) | Notes (if applicable) |
| user_profile | [models.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/models.py) | ![screenshot](documentation/validation/py-user_profile-models.png) | Notes (if applicable) |
| user_profile | [urls.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/urls.py) | ![screenshot](documentation/validation/py-user_profile-urls.png) | Notes (if applicable) |
| user_profile | [views.py](https://github.com/marijavelickovska/grow_healthy/blob/main/user_profile/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marijavelickovska/grow_healthy/main/user_profile/views.py) | ![screenshot](documentation/validation/py-user_profile-views.png) | Notes (if applicable) |


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

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both *mobile* and *desktop*.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Add Blog | ![screenshot](documentation/lighthouse/mobile-add-blog.png) | ![screenshot](documentation/lighthouse/desktop-add-blog.png) |
| Edit Blog | ![screenshot](documentation/lighthouse/mobile-edit-blog.png) | ![screenshot](documentation/lighthouse/desktop-edit-blog.png) |
| Blog Post | ![screenshot](documentation/lighthouse/mobile-blog-post.png) | ![screenshot](documentation/lighthouse/desktop-blog-post.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Blog Management | Feature is expected to allow the blog owner to create new posts with a title, featured image, and content. | Created a new post with valid title, image, and content data. | Post was created successfully and displayed correctly in the blog. | ![screenshot](documentation/defensive/create-post.png) |
| | Feature is expected to allow the blog owner to update existing posts. | Edited the content of an existing blog post. | Post was updated successfully with the new content. | ![screenshot](documentation/defensive/update-post.png) |
| | Feature is expected to allow the blog owner to delete blog posts. | Attempted to delete a blog post, confirming the action before proceeding. | Blog post was deleted successfully. | ![screenshot](documentation/defensive/delete-post.png) |
| | Feature is expected to retrieve a list of all published posts. | Accessed the blog owner dashboard to view all published posts. | All published posts were displayed in a list view. | ![screenshot](documentation/defensive/published-posts.png) |
| | Feature is expected to preview posts as drafts before publishing. | Created a draft post and previewed it. | Draft was displayed correctly in preview mode. | ![screenshot](documentation/defensive/preview-draft.png) |
| Comments Management | Feature is expected to allow the blog owner to approve or reject comments. | Approved and rejected comments from the dashboard. | Approved comments were published; rejected comments were removed. | ![screenshot](documentation/defensive/review-comments.png) |
| | Feature is expected to allow the blog owner to edit or delete comments. | Edited and deleted existing comments. | Comments were updated or removed successfully. | ![screenshot](documentation/defensive/edit-delete-comments.png) |
| User Authentication | Feature is expected to allow registered users to log in to the site. | Attempted to log in with valid and invalid credentials. | Login was successful with valid credentials; invalid credentials were rejected. | ![screenshot](documentation/defensive/login.png) |
| | Feature is expected to allow users to register for an account. | Registered a new user with unique credentials. | User account was created successfully. | ![screenshot](documentation/defensive/register.png) |
| | Feature is expected to allow users to log out securely. | Logged out and tried accessing a restricted page. | Access was denied after logout, as expected. | ![screenshot](documentation/defensive/logout.png) |
| User Comments | Feature is expected to allow registered users to leave comments on blog posts. | Logged in and added comments to a blog post. | Comments were successfully added and marked as pending approval. | ![screenshot](documentation/defensive/add-comment.png) |
| | Feature is expected to display a notification that comments are pending approval. | Added a comment and checked the notification message. | Notification was displayed as expected. | ![screenshot](documentation/defensive/pending-approval.png) |
| | Feature is expected to allow users to edit their own comments. | Edited personal comments. | Comments were updated as expected. | ![screenshot](documentation/defensive/edit-user-comments.png) |
| | Feature is expected to allow users to delete their own comments. | Deleted personal comments. | Comments were removed as expected. | ![screenshot](documentation/defensive/delete-user-comments.png) |
| Guest Features | Feature is expected to allow guest users to read blog posts without registering. | Opened blog posts as a guest user. | Blog posts were fully accessible without logging in. | ![screenshot](documentation/defensive/view-posts-guest.png) |
| | Feature is expected to display the names of other commenters on posts. | Checked the names of commenters on posts as a guest user. | Commenter names were displayed as expected. | ![screenshot](documentation/defensive/commenter-names.png) |
| | Feature is expected to block standard users from brute-forcing admin pages. | Attempted to navigate to admin-only pages by manipulating the URL (e.g., `/admin`). | Access was blocked, and a message was displayed showing denied access. | ![screenshot](documentation/defensive/brute-force.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a blog owner | I would like to create new blog posts with a title, featured image, and content | so that I can share my experiences with my audience. | ![screenshot](documentation/features/feature01.png) |
| As a blog owner | I would like to update existing blog posts | so that I can correct or add new information to my previous stories. | ![screenshot](documentation/features/feature02.png) |
| As a blog owner | I would like to delete blog posts | so that I can remove outdated or irrelevant content from my blog. | ![screenshot](documentation/features/feature03.png) |
| As a blog owner | I would like to retrieve a list of all my published blog posts | so that I can manage them from a central dashboard. | ![screenshot](documentation/features/feature04.png) |
| As a blog owner | I would like to preview a post as draft before publishing it | so that I can ensure formatting and content appear correctly. | ![screenshot](documentation/features/feature05.png) |
| As a blog owner | I would like to review comments before they are published | so that I can filter out spam or inappropriate content. | ![screenshot](documentation/features/feature06.png) |
| As a blog owner | I would like to approve or reject comments from users | so that I can maintain control over the discussion on my posts. | ![screenshot](documentation/features/feature07.png) |
| As a blog owner | I would like to view a list of all comments (both approved and pending) | so that I can manage user engagement effectively. | ![screenshot](documentation/features/feature08.png) |
| As a blog owner | I would like to edit or delete user comments | so that I can clean up or remove inappropriate responses after they've been posted. | ![screenshot](documentation/features/feature09.png) |
| As a registered user | I would like to log in to the site | so that I can leave comments on blog posts. | ![screenshot](documentation/features/feature10.png) |
| As a registered user | I would like to register for an account | so that I can become part of the community and engage with the blog. | ![screenshot](documentation/features/feature11.png) |
| As a registered user | I would like to leave a comment on a blog post | so that I can share my thoughts or ask questions about the owner's experiences. | ![screenshot](documentation/features/feature12.png) |
| As a registered user | I would like my comment to show my name and the timestamp | so that others can see who I am and when I left the comment. | ![screenshot](documentation/features/feature13.png) |
| As a registered user | I would like to receive a notification or message saying my comment is pending approval | so that I understand it hasn't been posted immediately. | ![screenshot](documentation/features/feature14.png) |
| As a registered user | I would like to edit or delete my own comments | so that I can fix mistakes or retract my statement. | ![screenshot](documentation/features/feature15.png) |
| As a guest user | I would like to read blog posts without registering | so that I can enjoy the content without needing to log in. | ![screenshot](documentation/features/feature16.png) |
| As a guest user | I would like to browse past posts | so that I can explore the blog's full content history. | ![screenshot](documentation/features/feature17.png) |
| As a guest user | I would like to register for an account | so that I can participate in the community by leaving comments on posts. | ![screenshot](documentation/features/feature18.png) |
| As a guest user | I would like to see the names of other commenters on posts | so that I can get a sense of community interaction before registering. | ![screenshot](documentation/features/feature19.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/feature20.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/marijavelickovska/grow_healthy/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Amarijavelickovska%2Fgrow_healthy%20label%3Abug&label=bugs)](https://www.github.com/marijavelickovska/grow_healthy/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/marijavelickovska/grow_healthy/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/marijavelickovska/grow_healthy/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issues](https://img.shields.io/github/issues/marijavelickovska/grow_healthy)](https://www.github.com/marijavelickovska/grow_healthy/issues)

Any remaining open issues can be tracked [here](https://www.github.com/marijavelickovska/grow_healthy/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling. | ![screenshot](documentation/issues/overflow.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

