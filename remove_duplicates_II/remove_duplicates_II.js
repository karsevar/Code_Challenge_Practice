var removeDuplicates = function (nums) {
  // most likely for this problem I might need to use two pointers
  // the first pointer will be the main iterator of the outer loop
  // while the second pointer will be used to increment according to the
  // reoccurance of outer pointer's value
  // then the two pointers will give me the range to which I should delete values

  let pointer_outer = 0;

  while (pointer_outer < nums.length) {
    let pointer_inner = pointer_outer + 1;
    let counter = 1;
    if (nums[pointer_outer] === nums[pointer_inner]) {
      while (nums[pointer_inner] === nums[pointer_outer]) {
        counter += 1;
        if (counter > 2) {
          nums.splice(pointer_inner, 1);
        } else {
          pointer_inner += 1;
        }
      }
    }
    pointer_outer = pointer_inner;
  }
};
