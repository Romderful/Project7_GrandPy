const userInput = $("#user-input");
const chatZone = $("#chat-zone");
let mapIndex = 0;

$("form").keypress(function (event) {
    const text = userInput.val();
    if (event.keyCode === 13) {
        if (text.length <= 1) {
            userInput.val("");
        } else {
            chatZone.append(`<p class="user-text">${text}</p>`);
            ajaxPost(text);
            userInput.val("");
        };
    };
});

function ajaxPost(text) {
    $.ajax({
        method: "POST",
        url: "/process",
        data: { data: text },
        success: function (response) {
            if (response["coordinates"]) {
                chatZone.append(`<div class="map" id="map${mapIndex}"></div>`);
                createMap(response["coordinates"], response["here_js_api_key"]);
            } else {
                chatZone.append(
                    `<p class="bot-answer">Oops, je n'ai rien trouvé, pourrais-tu essayer d'être plus précis s'il te plait ?
                    C'est que je commence à me faire vieux.</p>`
                )
            };
        },
    })
};

function createMap(coordinates, api_key) {
    let platform = new H.service.Platform({
        apikey: api_key
    });
    let defaultLayers = platform.createDefaultLayers();
    let map = new H.Map(document.querySelector(`#map${mapIndex}`),
        defaultLayers.raster.normal.map, {
        engineType: H.map.render.RenderEngine.EngineType.P2D
    });
    window.addEventListener('resize', () => map.getViewPort().resize());
    let marker = new H.map.Marker(coordinates);
    new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
    H.ui.UI.createDefault(map, defaultLayers);
    map.addObject(marker);
    map.setCenter(coordinates);
    map.setZoom(12);
    mapIndex++;
}
