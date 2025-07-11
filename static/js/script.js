/* On click on a card with the class card-home, 
 * a message is displayed and the page scrolls to the #join_us section where the message appears. 
 * The message disappears after 5 seconds. */ 

let cards = document.getElementsByClassName("card-home");
for (let card of cards) {
	card.addEventListener("click", showRecipeMessage);
}

function showRecipeMessage() {
	let messageDiv = document.getElementById("join-us-message");
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


/* On click on the edit button, enable profile form editing 
 * by unlocking inputs and showing image upload and save options. */ 
const editBtn = document.getElementById("editBtn");
const saveBtn = document.getElementById("saveBtn");
const nameInput = document.getElementById("nameInput");
const aboutInput = document.getElementById("aboutInput");
const imageInput = document.getElementById("profileImgInput");
const chooseImageLabel = document.getElementById("chooseImageLabel");

editBtn.addEventListener("click", function () {
    nameInput.removeAttribute("disabled");
    aboutInput.removeAttribute("disabled");

    imageInput.classList.remove("d-none");
    chooseImageLabel.classList.remove("d-none");
    saveBtn.classList.remove("d-none");
    editBtn.classList.add("d-none");
});


/* On click on submit comment button, scroll to the top of the comments section 
 * where the new comment appears.*/ 
document.getElementById("submitCommentButton").addEventListener("click", function () {
    const commentsSection = document.getElementById("comments");
    if (commentsSection) {
        commentsSection.scrollIntoView({ behavior: "smooth" });
    }
});


/* Adds click listeners to edit buttons that load the selected comment into the form for editing, 
 * change the submit button text to "Update," update the form action URL, 
 * and scroll to the top of the comments section where the updated comment appears.*/ 
const editCommentButtons = document.getElementsByClassName("btn-edit-comment");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitCommentButton = document.getElementById("submitCommentButton");

for (let button of editCommentButtons) {
	button.addEventListener("click", (e) => {
		let commentId = e.currentTarget.getAttribute("data-comment_id");
		let recipeId = e.currentTarget.getAttribute("data-recipe_id");
		let commentContent = document.getElementById(`comment${commentId}`).innerText;
		commentText.value = commentContent;
		submitCommentButton.innerText = "Update";
		commentForm.setAttribute("action", `/user_profile/recipe/${recipeId}/edit_comment/${commentId}/`);

		const commentSection = document.getElementById("add_comment");
		if (commentSection) {
			commentSection.scrollIntoView({
				behavior: "smooth"
			});
		}
	});
}


/* On click on delete button on a comment, open a Bootstrap modal for confirming comment deletion, 
 * updates modal text and form action URL, and shows the modal for user confirmation. */ 
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteForm = document.getElementById("deleteForm");
const deleteModalBody = document.getElementById("deleteModalBody");
const deleteModalTitle = document.getElementById("deleteModalTitle");

const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");
for (let button of deleteCommentButtons) {
	button.addEventListener("click", (e) => {
		let commentId = e.currentTarget.getAttribute("data-comment_id");
		let recipeId = e.currentTarget.getAttribute("data-recipe_id");

		deleteModalTitle.innerText = "Delete comment?";
		deleteModalBody.innerText = "Are you sure you want to delete your comment? This action cannot be undone.";
		deleteForm.action = `/user_profile/recipe/${recipeId}/delete_comment/${commentId}/`;

		deleteModal.show();
	});
}


/* On click on delete button on a recipe, open a Bootstrap modal for confirming recipe deletion, 
 * updates modal text and form action URL, and shows the modal for user confirmation. */ 
const deleteRecipeButtons = document.getElementsByClassName("btn-delete-recipe");
for (let button of deleteRecipeButtons) {
	button.addEventListener("click", (e) => {
		let recipeId = e.currentTarget.getAttribute("data-recipe_id");

		deleteModalTitle.innerText = "Delete recipe?";
		deleteModalBody.innerText = "Are you sure you want to delete this recipe? This action cannot be undone.";
		deleteForm.action = `/user_profile/delete_recipe/${recipeId}/`;

		deleteModal.show();
	});
}
