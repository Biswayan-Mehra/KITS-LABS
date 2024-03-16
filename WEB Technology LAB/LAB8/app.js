var app = angular.module("gradeCalculatorApp", []);

app.controller("GradeCalculatorController", function ($scope) {
  $scope.calculateGrade = function () {
    var course1Marks = parseFloat($scope.course1Marks);
    var course2Marks = parseFloat($scope.course2Marks);
    var course3Marks = parseFloat($scope.course3Marks);
    var course4Marks = parseFloat($scope.course4Marks);
    var course5Marks = parseFloat($scope.course5Marks);

    if (
      !isNaN(course1Marks) &&
      !isNaN(course2Marks) &&
      !isNaN(course3Marks) &&
      !isNaN(course4Marks) &&
      !isNaN(course5Marks)
    ) {
      var totalMarks =
        course1Marks +
        course2Marks +
        course3Marks +
        course4Marks +
        course5Marks;
      var average = totalMarks / 5;
      var grade = "";

      if (average > 95) {
        grade = "S";
      } else if (average > 85 && average <= 95) {
        grade = "A";
      } else if (average > 75 && average <= 85) {
        grade = "B";
      } else if (average > 65 && average <= 75) {
        grade = "C";
      } else if (average > 50 && average <= 65) {
        grade = "P";
      } else {
        grade = "F";
      }

      $scope.average = average;
      $scope.grade = grade;
    } else {
      alert("Please enter valid marks for all courses.");
    }
  };
});
