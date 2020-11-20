var my = angular.module('name' , [])

my.run(function(){
	//run immediate after program runs
})
my.controller('nameCon',function($scope)
{
	$scope.msg = 'hloo! i am Ved Gupta. Founder and C.E.O of Next Innovation';
	$scope.nam = 'Ved Prakash Gupta';
	$scope.friends = ['Ved Gupta' , 'Sudhanshu Srivastava' , 'Ajay Sharma' , 'Anchal' , 'Amit Prajapati'];
	$scope.detail_of_friend = [
	{ 
		name : 'ved',
		color : 'blue',
		Salery : 200
	},
	{ 
		name : 'Ajay',
		color : 'green',
		Salery : 300
	},
	{ 
		name : 'Sudhanshu',
		color : 'black',
		Salery : 300
	},
	{ 
		name : 'Anchal',
		color : 'violet',
		Salery : 250
	},
	];
})