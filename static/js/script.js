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


