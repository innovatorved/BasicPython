var ass4 = angular.module("file" , ['ngRoute']);

ass4.config(["$routeProvider" , function($routeProvider)
{
	$routeProvider
	.when('/form',{ templateUrl : "form.html"})

}]);

