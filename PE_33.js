// Problem 33 - second in Javascript
// 9/24/14

var canceling = function(a,b){
  if (a.toString()[1] == 0 || b.toString()[1] == 0 || a == b)
    return false
  else if (a.toString()[1] == b.toString()[0])
  	return (+a.toString()[0])/(+b.toString()[1]);
  else if (a.toString()[0] == b.toString()[1])
  	return (+a.toString()[1])/(+b.toString()[0]);
  else if (a.toString()[0] == b.toString()[0])
  	return (+a.toString()[1])/(+b.toString()[1]);
  else if (a.toString()[1] == b.toString()[1])
  	return (+a.toString()[0])/(+b.toString()[0]);
  else
    return false;
}

var output = function(){
  var listOfC = [];
  for(var a = 10; a<50; a++){
    for(var b = 10; b<100; b++){
      if (canceling(a,b) === a/b){
        listOfC.push(a/b);
      }
    }
  }
  return listOfC.reduce(function(a, b) { return a * b; }, 1);
}

console.log(output());
