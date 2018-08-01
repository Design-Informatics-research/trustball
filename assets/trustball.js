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
	if (n == 1) {
		document.getElementById("context").innerHTML = "The Health Service wants to share your data for research purposes.";
	}
	if (n == 2) {
		document.getElementById("context").innerHTML = "The Bank wants to share your data for research purposes.";
	}
	if (n == 3) {
		document.getElementById("context").innerHTML = "Your employer wants to share your data for research purposes.";
	}
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
  var n = kn - 48;
  if ((n >= 1) && (n <= 6)){
    return n;
  } 
  else {
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