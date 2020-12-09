var removeDuplicates = function (nums) {
  i = 1;

  while (nums.length > i) {
    if (nums[i - 1] == nums[i]) {
      nums.splice(i, 1);
    } else {
      i += 1;
    }
  }
};
