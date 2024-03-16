var element;
var timer;
var pillar;

function sayWelcome() {
  alert("Welcome to Car Animation");
}

function init() {
  element = document.getElementById("box");
  element.style.position = "relative";
  element.style.left = "2px";
  pillar = document.getElementById("pillar");
}

function startAnime() {
  if (!element || !pillar) {
    init();
  }

  var currentPosition = parseInt(element.style.left);

  if (currentPosition + element.width >= pillar.offsetLeft) {
    stopAnime();
    alert("Danger! Animation stopped.");
  } else {
    element.style.left = currentPosition + 1 + "px";
    timer = setTimeout(startAnime);
  }
}

function stopAnime() {
  clearTimeout(timer);
}

function resetPosition() {
  if (element) {
    element.style.left = "2px";
  }
}
