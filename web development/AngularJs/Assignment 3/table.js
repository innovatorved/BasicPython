var fri = angular.module('detail' , [])
fri.config(function()
{
	//config rum br=efore the program runs
})
fri.run(function(){
	//run immediate after program runs
})
fri.controller('details',function($scope)
{
	$scope.msg = 'project successfully done';
	//$scope.nam = 'Ved Prakash Gupta';
	//$scope.friends = ['Ved Gupta' , 'Sudhanshu Srivastava' , 'Ajay Sharma' , 'Anchal' , 'Amit Prajapati'];
	$scope.detail_of_friend = [
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
		name : 'Anchal',
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