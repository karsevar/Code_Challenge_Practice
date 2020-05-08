var isValid = function (str) {
  // first create a stack (which will just be an array)

  // split the string into an array (for easier parsing)

  // create an object that will contain the opening brackets as
  // the key and the closing equivalent as the value

  // create a for loop that will loop through the string array
  // if current value in the index is a key in the bracket object
  // push the current value in the stack

  // else if the current value is in bracket array values
  // pop from the stack and check if the popped value reversed
  // is equal to the current value
  // if not return false

  // return true

  if (str === undefined) {
    return false;
  }

  let stack = [];
  const str_array = str.split("");
  const reversed_bracket = {
    "[": "]",
    "{": "}",
    "(": ")",
  };

  // check if the str_array is empty
  // if yes return false
  if (str_array.length === 0) {
    return true;
  }

  if (str_array.length === 1) {
    return false;
  }

  let stack_counter = 0;

  for (let index = 0; index < str_array.length; index++) {
    if (reversed_bracket.hasOwnProperty(str_array[index]) === true) {
      stack.push(str_array[index]);
      stack_counter += 1;
    } else if (
      Object.values(reversed_bracket).indexOf(str_array[index]) !== -1
    ) {
      // console.log(`closing bracket found ${str_array[index]}`)
      let popped_value = stack.pop();

      if (reversed_bracket[popped_value] !== str_array[index]) {
        return false;
        // console.log(`match found ${popped_value} ${str_array[index]}`)
      }
    }
  }

  // console.log(reversed_bracket['['])
  return true;
};

isValid("(the thing )");
