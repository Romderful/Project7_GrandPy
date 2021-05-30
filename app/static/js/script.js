const userInput = $("#userInput");
const chatZone = $("#chatZone");

$("form").keypress(function (event) {
    const text = userInput.val();
    if (event.keyCode === 13) {
        chatZone.append(`<p>${text}</p>`);
        userInput.val("");
        sendUserInput(text);
    };
});

function sendUserInput(text) {
    $.ajax({
        method: "POST",
        url: "/process",
        data: { data: text },
        success: function (response) {
            console.log(response);
        },
        error: function (error) {
            console.log(error);
        }
    })
};
