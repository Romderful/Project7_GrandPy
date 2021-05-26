const userInput = $("#userInput");
const chatZone = $("#chatZone");

$("form").keypress(function (event) {
    if (event.keyCode === 13) {
        const text = userInput.val();
        chatZone.append(`<p>${text}</p>`);
        userInput.val("");
        sendAjax(text);
    };
});

function sendAjax(text) {
    $.ajax({
        method: "POST",
        url: "/process",
        data: { data: text }
    })
};
