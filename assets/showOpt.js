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