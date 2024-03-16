angular
  .module("productInventoryApp", [])
  .controller("ProductInventoryController", function ($scope) {
    $scope.products = [
      { name: "Product 1", price: 10.99 },
      { name: "Product 2", price: 24.99 },
      { name: "Product 3", price: 19.99 },
      { name: "Product 4", price: 29.99 },
      { name: "Product 5", price: 14.99 },
    ];

    $scope.addProduct = function () {
      if ($scope.name && $scope.price) {
        $scope.products.push({ name: $scope.name, price: $scope.price });
      }
    };

    $scope.deleteProduct = function (index) {
      $scope.products.splice(index, 1);
    };
  });
