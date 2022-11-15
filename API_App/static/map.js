const attribution =
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const map = L.map("map");
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: attribution,
}).addTo(map);
map.setView([49.256, 4.146], 8);


// get coordinates of corners of the div when map is moved
map.on("moveend", function () {
    const bounds = map.getBounds();
    const sw = bounds.getSouthWest();
    const ne = bounds.getNorthEast();
    const sw_lat = sw.lat;
    const sw_lng = sw.lng;
    const ne_lat = ne.lat;
    const ne_lng = ne.lng;
    console.log(sw_lat, sw_lng, ne_lat, ne_lng);

    const url = "http://127.0.0.1:8000/spots/?northEastLat="+ne_lat+"&northEastLong="+ ne_lng +"&southWestLat="+sw_lat+"&southWestLong="+sw_lng;
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        console.log("listlonglat", data["Polygon"]);
        //var polygon = L.polygon(data["Polygon"], {color: 'red'}).addTo(map);
        // add marker for each spot
        for (let i = 0; i < data["Points"].length; i++) {
            const spot = data["Points"][i];
            console.log(spot["coordinates"]);
            const marker = L.marker(spot["coordinates"]).addTo(map);
        }

});
});




