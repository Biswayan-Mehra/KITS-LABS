$(document).ready(function () {
  $("#calculate").click(function () {
    var day = parseInt($("#day").val());
    var month = parseInt($("#month").val());
    var year = parseInt($("#year").val());

    var birthdate = new Date(year, month - 1, day);
    var today = new Date();

    if (isNaN(birthdate.getTime())) {
      alert("Invalid date. Please enter a valid date.");
      return;
    }

    var ageInMilliseconds = today - birthdate;
    var ageInSeconds = ageInMilliseconds / 1000;
    var ageInMinutes = ageInSeconds / 60;
    var ageInHours = ageInMinutes / 60;
    var ageInDays = ageInHours / 24;

    var years = Math.floor(ageInDays / 365);
    var months = Math.floor((ageInDays % 365) / 30);
    var days = Math.floor((ageInDays % 365) % 30);

    $("#years").text(years);
    $("#months").text(months);
    $("#days").text(days);
  });
});
