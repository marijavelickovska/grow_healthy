const editCommentButtons = document.getElementsByClassName("btn-edit-comment");
const commentText = document.getElementById("id_body"); 
const commentForm = document.getElementById("commentForm");
const submitCommentButton = document.getElementById("submitCommentButton");

const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");
const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteCommentConfirm = document.getElementById("deleteConfirm");


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


for (let button of deleteCommentButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("data-comment_id");
    let recipeId = e.currentTarget.getAttribute("data-recipe_id");
    deleteCommentConfirm.href = `/user_profile/recipe/${recipeId}/delete_comment/${commentId}/`; 
    deleteCommentModal.show();
  });
}


