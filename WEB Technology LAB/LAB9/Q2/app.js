var app = angular.module("myApp", ["ngRoute"]);

app.config(function ($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "/LAB9/Q2/personal.html",
    })
    .when("/personal", {
      templateUrl: "/LAB9/Q2/personal.html",
    })
    .when("/academic", {
      templateUrl: "/LAB9/Q2/academic.html",
    })
    .when("/project", {
      templateUrl: "/LAB9/Q2/project.html",
    })
    .when("/login", {
      templateUrl: "/LAB9/Q2/login.html",
    })
    .when("/signup", {
      templateUrl: "/LAB9/Q2/signup.html",
    })
    .otherwise({ redirectTo: "/" });
});
