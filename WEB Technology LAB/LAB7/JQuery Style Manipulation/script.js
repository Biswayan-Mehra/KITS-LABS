$(document).ready(function () {
  const box = $("#box");

  $(".btn").click(function () {
    const effect = $(this).attr("id");
    switch (effect) {
      case "showBtn":
        box.show("slow");
        break;
      case "hideBtn":
        box.hide("slow");
        break;
      case "toggleBtn":
        box.toggle("slow");
        break;
      case "fadeInBtn":
        box.fadeIn("slow");
        break;
      case "fadeOutBtn":
        box.fadeOut("slow");
        break;
      case "fadeToggleBtn":
        box.fadeToggle("slow");
        break;
      case "slideUpBtn":
        box.slideUp("slow");
        break;
      case "slideDownBtn":
        box.slideDown("slow");
        break;
      case "slideToggleBtn":
        box.slideToggle("slow");
        break;
      case "animateBtn":
        box.animate(
          {
            width: "toggle",
            height: "toggle",
            fontSize: "toggle",
          },
          "slow"
        );
        break;
    }
  });
});
