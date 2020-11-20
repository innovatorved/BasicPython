var dat = angular.module("data" , ['ngRoute']);

dat.config(["$routeProvider" , function($routeProvider)
{
	$routeProvider
	.when('/book',{ templateUrl : "view/Book.html" , controller : "dataCon"})

	.when('/clo',{ templateUrl : "view/Clothes.html" , controller : "dataCon"})

	.when('/com',{ templateUrl : "view/Company.html" , controller : "dataCon"})

	.when('/food',{ templateUrl : "view/food.html" , controller : "dataCon"})
}]);

dat.controller("dataCon" , function($scope)
{
	$scope.readMe = "Controller Succesfull Created !";

	$scope.Books = ["Vector Infinity" , "you Are the Hell's king" , "New Era was Started" , "Welcome to My Word" ,"She so Importent for He !"];

	$scope.Clothes = ["Sari" , "Salwaar Kameez" , "Dhoti" , "Panche or Lungi." ,"Achkan/Sherwani"];

	$scope.Company = ["Tata Consultancy Services" , "Infosys" , "Wipro" , "HCL Technologies" , "Tech Mahindra"];

	$scope.Food = ["Chana masala" , "Daal baati churma" , "Dal makhani (kali dal)" , "Dal fara" , "Dum aloo"];
});
