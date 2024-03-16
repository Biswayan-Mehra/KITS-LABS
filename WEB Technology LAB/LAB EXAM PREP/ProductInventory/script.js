angular.module("myApp", []).controller("myController", function ($scope) {
  $scope.products = [
    { name: "Lamborgini", price: 200000 },
    { name: "Bugatti", price: 1000000 },
  ];
  $scope.addProduct = function () {
    $scope.products.push({ name: $scope.name, price: $scope.price });
  };
  $scope.removeRow = function (index) {
    $scope.products.splice(index, 1);
  };
});
