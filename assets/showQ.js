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