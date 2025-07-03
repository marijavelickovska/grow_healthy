document.addEventListener("DOMContentLoaded", function () {
   let cards = document.getElementsByClassName("card-home");

    for (let card of cards) {
        card.addEventListener("click", showRecipeMessage);
    }

});


//na klik na cards da se pokazuva porakata za login na home page 
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

