var start = document.getElementById("start");
var stop = document.getElementById("stop");
var video = document.getElementById("video");

start.onclick = function() {
    start.style.display = "none";
    stop.style.display = "inline";
    fetch("/start").then(response => response.text()).then(data => {
        console.log(data);
    });
    fetch("/video");
    document.getElementById("frame").src='/video';
};

stop.onclick = function() {
    stop.style.display = "none";
    start.style.display = "inline";
    document.getElementById("frame").src="/static/images/swe.png";
    fetch("/stop").then(response => response.text()).then(data => {
        console.log(data);
    });
};