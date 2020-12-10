var combine = function (n, k) {
  const combinations = [];

  function recursionHelper(start, n, k, combination) {
    if (combination.length === k) {
      combinations.push(combination);
    } else {
      for (let i = start; i < n + 1; i++) {
        recursionHelper(i + 1, n, k, [...combination, i]);
      }
    }
  }
  recursionHelper(1, n, k, []);
  return combinations;
};
