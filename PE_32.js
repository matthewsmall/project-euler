//Problem 32 - my first one solved in Javascript
// 9/24/14

var pandigital = function(str){//only 9 digit strs are passed
  for (var i = 1; i < 10; i++) {
    if(str.indexOf(i) === -1){ 
     return false;
    }
  }
  //console.log(str);
  return true;
}

var output = function(loopLen){
  var c = 0;
  var nums = "";
  var listOfC = [];
  for(var a = 1; a<loopLen; a++){
    for(var b = 2; b<loopLen; b++){
      c = a * b;
      nums = a.toString() + b.toString() + c.toString();
      if (nums.length === 9){//do this check for speed
        if (pandigital(nums) === true){
          //console.log("a: " + a +", b: " + b + ", c = " + c);
          if(listOfC.indexOf(c) === -1){
            listOfC.push(c);
            //console.log(listOfC);
          }
        }
      }
    }
  }
  return listOfC.reduce(function(a, b) { return a + b; }, 0);
}

console.log(output(2000));
