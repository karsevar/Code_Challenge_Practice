// First try solution. Time complexity is a little messy because on top of
// finding all possible permutations of the dice according to the number of
// different faces I'm factoring in creating arrays and summing the contents
// together when the combination length reaches d values.

var numRollsToTarget = function (d, f, target) {
  // first create a counter variable that will keep count of every time
  // the sum of a face combination reaches the target amount

  // create a recursive function that will have d, f, target, and combination as the
  // arugments
  // base case:
  // if combination length is equal to d and target is zero
  // increment the counter by one
  // recursive case:
  // if combination length is less than d
  // create a for loop that will loop through all the faces in the
  // dice and call the recursive function

  let counter = 0;

  const recursiveHelper = (d, f, target, combination = null) => {
    if (combination !== null && combination.length === d) {
      const combinationSum = combination.reduce((a, b) => {
        return a + b;
      }, 0);

      if (combinationSum === target) {
        counter += 1;
      }
    } else {
      for (let i = 1; f + 1 > i; i++) {
        let newCombination = [];
        if (combination === null) {
          newCombination.push(i);
        } else {
          newCombination = [...combination, i];
        }
        recursiveHelper(d, f, target, newCombination);
      }
    }
  };

  recursiveHelper(d, f, target);
  return counter;
};

// Cut down on some of the time complexity of the last solution but this
// implementation still fails the d = 50, f = 50 and target=500 test case
// will need to find a better algorithmic solution that lends itself to memorization

var numRollsToTarget = function (d, f, target) {
  let counter = 0;

  const recursiveHelper = (d, f, target, combination = 0) => {
    if (combination === d && target === 0) {
      counter += 1;
    } else if (combination < d && target > 0) {
      for (let i = 1; f + 1 > i; i++) {
        let newCombination = combination + 1;
        recursiveHelper(d, f, target - i, newCombination);
      }
    }
  };

  recursiveHelper(d, f, target);
  return counter;
};
