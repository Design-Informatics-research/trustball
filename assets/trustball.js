var options = ["Myself", "Friend", "Expert", "Crowd", "AI Bot"];
var timeoutId;

function shuffle(array) {
	var currentIndex = array.length, temporaryValue, randomIndex;
			
	while (0 !== currentIndex) {
		randomIndex = Math.floor(Math.random() * currentIndex);
		currentIndex -= 1;

		temporaryValue = array[currentIndex];
		array[currentIndex] = array[randomIndex];
		array[randomIndex] = temporaryValue;
   	}

	return array;
}

function showQ(n){
	var contexts = ["A game asks you to share music playlists and listening habits to develop an algorithm to change in-game-music according to your taste and mood.",
		"Your weather app request access to your location and  audio data to investigate noise pollution in your city. This data will be shared with the local council to review speed limits.",
		"Your sibling shares a survey with you to plan a joint holiday. They use an online service that asks for access to your entire browser history.", 
		"Your boss requires you to download a new chat service to communicate with your colleagues. You download the service and it asks for access to all your contacts in your address book, not only work-related ones. If you don’t agree, you can’t use the service for work.",
		"To provide personalised food boxes, local producers ask you to share social media likes of food pictures.",
		"Public health services ask you share anonymized  medical records with third parties to improve services."];
	document.getElementById("context").innerHTML = contexts[n-1];
}

function showOPt(seqImg, seqCap, opt){
	var img = document.getElementById(seqImg);
	
	if (opt == "lollipop") {
		img.src = "../assets/img1.png";
		document.getElementById(seqCap).innerHTML = "Lollipop";
	}
	if (opt == "icecream") {
		img.src = "../assets/img2.png";
		document.getElementById(seqCap).innerHTML = "Ice Cream";
	}
	if (opt == "chips") {
		img.src = "../assets/img3.png";
		document.getElementById(seqCap).innerHTML = "Chips";
	}
	if (opt == "donut") {
		img.src = "../assets/img4.png";
		document.getElementById(seqCap).innerHTML = "Donut";
	}
	if (opt == "pizza") {
		img.src = "../assets/img5.png";
		document.getElementById(seqCap).innerHTML = "Pizza";
	}
}

var numberPress = function(kn){
	window.clearTimeout(timeoutId);
	var n = kn - 48;
	if ((n >= 1) && (n <= 6)){
		return n;
	} else {
		return false;
	}
};

function fadeout(n){
	if (n == 1){
		$("#opt2").fadeTo(2000,0);
		$("#opt3").fadeTo(2000,0);
		$("#opt4").fadeTo(2000,0);
		$("#opt5").fadeTo(2000,0);
	}
	if (n == 2){
		$("#opt1").fadeTo(2000,0);
		$("#opt3").fadeTo(2000,0);
		$("#opt4").fadeTo(2000,0);
		$("#opt5").fadeTo(2000,0);
	}
	if (n == 3){
		$("#opt1").fadeTo(2000,0);
		$("#opt2").fadeTo(2000,0);
		$("#opt4").fadeTo(2000,0);
		$("#opt5").fadeTo(2000,0);
	}
	if (n == 4){
		$("#opt1").fadeTo(2000,0);
		$("#opt2").fadeTo(2000,0);
		$("#opt3").fadeTo(2000,0);
		$("#opt5").fadeTo(2000,0);
	}
	if (n == 5){
		$("#opt1").fadeTo(2000,0);
		$("#opt2").fadeTo(2000,0);
		$("#opt3").fadeTo(2000,0);
		$("#opt4").fadeTo(2000,0);
	}
}

var handleGameTimeout = function(){
	timeoutId = setTimeout(function(){
		localStorage.setItem("newGame", "newballs");
		$.get( "/cleanballs", function(data) {});
		window.location.href = "/";
	}, 40000);
}

$(document).ready(function(){
	$(document).keypress(function(e) {
		var n = numberPress(e.which);
		if (n == 6){
			$.get( "/cleanballs", function(data) {});
			window.location.href = "/";
		}
	});
});