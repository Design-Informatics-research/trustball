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