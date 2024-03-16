$(document).ready(function () {
  const box = $("#img");
  $("#toggleBtn").click(function () {
    box.toggle("slow");
  });
  $("#fadeToggleBtn").click(function () {
    box.fadeToggle("slow");
  });
  $("#slideToggleBtn").click(function () {
    box.slideToggle("slow");
  });
});
