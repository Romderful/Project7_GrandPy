const userInput = $("#userInput")

$(userInput).keypress(function (event) {
    if (event.keyCode === 13) {
        sendAjax();
    };
});

function sendAjax() {
    $.ajax({
        method: "POST",
        url: "/process",
        data: userInput
    })
};