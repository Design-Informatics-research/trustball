var numberPress = function(kn){
  var n = kn - 48;
  if ((n >= 1) && (n <= 6)){
    return n;
  } 
  else {
    return false;
  }
};

