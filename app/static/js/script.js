const chatZone = $("#chatZone");
const userInput = $("#userInput");

userInput.on("keydown", (event) => {
    if (event.keyCode === 13) {
        const text = userInput.val();
        chatZone.append(`<p>${text}</p>`);
        userInput.val("");
    }
})
