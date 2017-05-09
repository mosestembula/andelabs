function fizzBuzz(entry) {
  
if (Number.isInteger(entry)) {

    if(entry%15===0) { // 15 is the lcm and therefore a number has to divide by it so as to divide throughout the two
      return "FizzBuzz";
    }
    else if(entry%3 ===0) {
      return "Fizz";
    }
    else if(entry%5===0) {
      return "Buzz";
    }
    else {
      return entry;
    }
  }
  
  else {
  return "you need to enter an integer";
 } 
 }


/* this is yet another function that could possibly solve that.
this function finds whether a number is disible by 3, 5 or both. 
15 is the LCM and therefore this is the number that the given entry must divide in order to be able to divide all the 2 numbers 5 and 3 */
// function fizzBuzz(number){
//   return number % 15 == 0 ? "FizzBuzz" : number % 5 == 0 ? "Buzz" :
//   number % 3 == 0 ? "Fizz" : number;
// };