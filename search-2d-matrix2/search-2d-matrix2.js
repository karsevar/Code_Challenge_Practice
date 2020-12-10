var searchMatrix = function (matrix, target) {
  // it seems like this problem might require a binary search algorithm as
  // a means to find the search row as well as find the specific cell in the
  // search column.
  for (let i = 0; matrix.length > i; i++) {
    if (binarySearch(target, matrix[i])) {
      return true;
    }
  }
  return false;
};

function binarySearch(target, array) {
  let low = 0;
  let high = array.length - 1;

  while (low <= high) {
    let mid = Math.floor((high + low) / 2);

    if (array[mid] === target) {
      return true;
    }

    if (array[mid] > target) {
      high = mid - 1;
    } else if (array[mid] < target) {
      low = mid + 1;
    }
  }
  return false;
}
