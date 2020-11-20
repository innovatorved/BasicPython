var me = angular.module("myinfo" , ['ngRoute' , 'ngAnimate']);

me.config(["$routeProvider" , function($routeProvider)
{
	$routeProvider
	.when('/',{ templateUrl : "view/home.html" , controller : "dataCon"})

	.when('/movie',{ templateUrl : "view/movie.html" , controller : "dataCon"})

	.when('/tv',{ templateUrl : "view/tv.html" , controller : "dataCon"})

	.when('/tech',{ templateUrl : "view/tech.html" , controller : "dataCon"})

	.when('/Me',{ templateUrl : "view/me.html" , controller : "dataCon"})

	.otherwise({
		redirectTo: "/"
	})
}]);

me.controller("dataCon" , function($scope)
{
	$scope.home_p1 = ['Before we move on any further - ','Let me introduce myself.'];

	$scope.home_p2 = ['I am Ved Prakash Gupta. I am from Barabanki nearest to Lucknow.','I am pursuing a diploma in Electronic Engineering from the Prestigious Government Polytechnic Bahraich Institute.','I love to make IoT projects and Explore more of My self.'];

	$scope.movie_1 = ['Avengers: Age of Ultron' , ' Is a 2015 American superhero film based on the Marvel Comics superhero team the Avengers,',' produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.',' It is the sequel to The Avengers (2012) and the 11th film in the Marvel Cinematic Universe (MCU).'];

	$scope.movie_2 = ['Thugs of Hindostan' , ' Is a 2018 Indian Hindi-language action-adventure film written and directed by Vijay Krishna Acharya,' , ' and produced by Aditya Chopra under his banner Yash Raj Films.' , 'The film stars Amitabh Bachchan, Aamir Khan, Fatima Sana Shaikh and Katrina Kaif.'];

	$scope.movie_3 = ['khatarnak khiladi 2' , 'Is a 2014 Indian Tamil-language action thriller film directed by N. Lingusamy ','and produced under his banner Thirupathi Brothers.',' The film stars Suriya and Vidyut Jammwal in the lead roles,',' while Samantha , Manoj Bajpaee and Dalip Tahil appear in supporting characters.',' The project was materialized in October 2013, with the principal photography took place on 20 November 2013',' in Mumbai and Goa, and was completed in June 2014.'];

	$scope.tv_info = [
	{ 
		name : 'Phir Bhi Na Maane...Badtameez Dil',
		p1 : 'The story revolves around Abeer Malhotra, a successful and charming rockstar, and Meher Purohit.',
		p2 : 'During college, Abeer sets his eye on a simple, intellectual and pretty girl, Meher, and they subsequently get married at a young age and then get divorced.',
		p3 : 'Eight years later, Meher returns in his life as the new CEO of the music channel he sings for. '

	},
	{ 
		name : 'Internet Wala Love',
		p1 : 'Internet Wala Love (transl. Love via Internet) is an Indian Hindi-language television drama show which aired on Colors TV from Internet Wala Love (transl. Love via Internet) is an Indian Hindi-language television drama show which aired on Colors TV from ',
		p2 : '27 August 2018 to 8 March 2019 before shifting to Colors Rishtey and concluding there on 29 March 2019.',
		p3 : 'Produced by Sunjoy Waddhwa under Sphere Origins, it starred Shivin Narang and Tunisha Sharma.'

	},
	{ 
		name : ' Sadda Haq. – My Life My Choice',
		p1 : 'Sadda Haq - My Life, My Choice (translation : Our Rights - My Life, My Choice) is an Indian television series',
		p2 : 'that premiered on Channel V India on 25 November 2013.',
		p3 : 'The Times of India said the show features characters from a range of areas across the country that are not common on television shows.'
		
	}]


	$scope.tech_info = [
	{ 
		name : 'Artificial intelligence',
		p1 : 'the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings.',
		p2 : 'The term is frequently applied to the project of developing systems endowed with the intellectual processes characteristic of humans, ',
		p3 : ' such as the ability to reason, discover meaning, generalize, or learn from past experience.'

	},
	{ 
		name : 'Internet of Things (IoT)',
		p1 : 'A network of Internet connected objects able to collect and exchange data.',
		p2 : 'It is commonly abbreviated as IoT. In a simple way to put it, You have "things" that sense and collect data and send it to the internet',
		p3 : 'Examples of objects that can fall into the scope of Internet of Things include connected security systems, thermostats, cars, electronic appliances, lights in household and more.'

	},
	{ 
		name : 'Machine learning',
		p1 : ' Is an application of artificial intelligence (AI) that provides systems the ability to automatically learn',
		p2 : 'and improve from experience without being explicitly programmed. ',
		p3 : 'Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.'
		
	}]

	$scope.tech_info = [
	{ 
		name : 'Artificial intelligence',
		p1 : 'the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings.',
		p2 : 'The term is frequently applied to the project of developing systems endowed with the intellectual processes characteristic of humans, ',
		p3 : ' such as the ability to reason, discover meaning, generalize, or learn from past experience.'

	},
	{ 
		name : 'Internet of Things (IoT)',
		p1 : 'A network of Internet connected objects able to collect and exchange data.',
		p2 : 'It is commonly abbreviated as IoT. In a simple way to put it, You have "things" that sense and collect data and send it to the internet',
		p3 : 'Examples of objects that can fall into the scope of Internet of Things include connected security systems, thermostats, cars, electronic appliances, lights in household and more.'

	},
	{ 
		name : 'Machine learning',
		p1 : ' Is an application of artificial intelligence (AI) that provides systems the ability to automatically learn',
		p2 : 'and improve from experience without being explicitly programmed. ',
		p3 : 'Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.'
		
	}]

	$scope.Food = ["Chana masala" , "Daal baati churma" , "Dal makhani (kali dal)" , "Dal fara" , "Dum aloo"];
});
