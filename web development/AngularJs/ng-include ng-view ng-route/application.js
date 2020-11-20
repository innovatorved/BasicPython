var nexti = angular.module("nextin",['ngRoute','ngAnimate']);

nexti.config(["$routeProvider",function($routeProvider)
{
	$routeProvider
	.when('/home',{ templateUrl : "home.html" })

	$routeProvider
	.when('/dir',{ templateUrl : "header.html" , controller: 'nextControl'})

	.otherwise({redirectTo : '/home'});
}]);

nexti.controller("nextControl" ,function($scope)
{
	$scope.msg = "You are now access Controller Part";
	$scope.nextinCustomers = [
	{ 
		name : 'Ved Gupta',
		color : 'blue',
		Salery : 2000,
		MobileNo : 7007868719,
		Gender : 'Male'
	},
	{ 
		name : 'Sudhanshu Srivastava',
		color : 'green',
		Salery : 3000,
		MobileNo : 7412580963,
		Gender : 'Male'
	},
	{ 
		name : 'Ajay Sharma',
		color : 'black',
		Salery : 3000,
		MobileNo : 4457786236,
		Gender : 'Male'
	},
	{ 
		name : 'Anchal Raj',
		color : 'violet',
		Salery : 2500,
		MobileNo : 7531598006,
		Gender : 'Male'
	},
	{
		name : 'Amit Prajapati',
		color : 'cyan',
		Salery : 3500,
		MobileNo : 8521634096,
		Gender : 'Male'
	}
	];
})

