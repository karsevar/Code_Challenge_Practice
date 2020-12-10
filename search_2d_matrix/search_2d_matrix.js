var searchMatrix = function (matrix, target) {
  // naive solution is to first loop through each column to see if the
  // target is within the range of the lowest and largest values if so
  // create an additional loop that will loop through each cell in the row
  // until the target is found

  // create a for loop that will loop through each individual column
  // create an if statement check that will check if the target falls
  // under the same range as the largest and smallest value in the row
  // if yes
  // create an additional loop that will loop through the row

  for (let i = 0; i < matrix.length; i++) {
    if (matrix[i][0] <= target && target <= matrix[i][matrix[i].length - 1]) {
      for (let j = 0; j < matrix[i].length; j++) {
        if (target === matrix[i][j]) {
          return true;
        }
      }
      return false;
    }
  }

  return false;
};
