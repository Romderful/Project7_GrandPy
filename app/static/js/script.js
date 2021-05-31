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
            chatZone.append('<div id="map"></div>');
            var platform = new H.service.Platform({
                apikey: "38g0LWQAVqN6jUp6xEEwQY9HTe2JF_GIr02m207HNYY"
            });
            var defaultLayers = platform.createDefaultLayers();

            var map = new H.Map(document.getElementById('map'),
                defaultLayers.vector.normal.map, {
                center: { lat: 50, lng: 5 },
                zoom: 4,
                pixelRatio: window.devicePixelRatio || 1
            });

            window.addEventListener('resize', () => map.getViewPort().resize());

            new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
            H.ui.UI.createDefault(map, defaultLayers);

            moveMap(map, response);
        },
        error: function (error) {
            console.log(error);
        }
    })
};

function moveMap(map, coordinates) {
    map.setCenter(coordinates);
    map.setZoom(14);
}
