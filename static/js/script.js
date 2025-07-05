const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body"); 
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");


// On DOMContentLoaded: Add event listener to cards to show a message when clicked
document.addEventListener("DOMContentLoaded", function () {
   let cards = document.getElementsByClassName("card-home");

    for (let card of cards) {
        card.addEventListener("click", showRecipeMessage);
    }

});


// Scroll to the section where the message is displayed and set a timeout to hide it
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


for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("data-comment_id");
    let recipeId = e.currentTarget.getAttribute("data-recipe_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `/user_profile/recipe/${recipeId}/edit_comment/${commentId}/`);
  });
}


