var car;
var pillar;
var timer;

function init() {
  car = document.getElementById("car");
  car.style.position = "relative";
  pillar = document.getElementById("pillar");
  car.style.left = "5px";
}

function startAnime() {
  if (!car || !pillar) {
    init();
  }
  var currentPosition = parseInt(car.style.left);
  if (currentPosition + car.width >= pillar.offsetLeft) {
    stopAnime();
    alert("Animation Stopped");
    resetAnime();
  } else {
    car.style.left = currentPosition + 1 + "px";
    timer = setTimeout(startAnime);
  }
}

function stopAnime() {
  clearTimeout(timer);
}

function resetAnime() {
  car.style.left = "5px";
}
