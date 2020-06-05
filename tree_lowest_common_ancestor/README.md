# Binary Search Tree: Lowest Common Ancestor

#### 1️⃣ Solution Summary

For my first attempt solution I used breadth first search to find the respective paths from the root node to the values assigned to the variables v1 and v2. Ultimately I iterated over the binary tree two different times to find the traversal paths to the variables v1 and v2. The traversal paths are both arrays (containing the node pointers from the root to the target node). After the breadth first search steps I compared the two path arrays and return the last matching pointer node between to two path arrays.

---

### Technologies Used

- Python

---

## 2️⃣ Challenge Information

| Title                                      | Challenge URL                                                                           | Time Complexity | Space Complexity | Difficulty |
| ------------------------------------------ | --------------------------------------------------------------------------------------- | --------------- | ---------------- | ---------- |
| Binary Search Tree: Lowest Common Ancestor | https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem | O(n)            | O(n)             | Easy       |

## 3️⃣ Time / Space Complexity

### Time Complexity

- O(n)

- Rationale:

  Though the rough time complexity estimate is O(n) for this solution it is important to know that this is only an approximation and doesn't mean that the algorithm is only iterating over the entire binary search tree once in the worst case (if the binary tree is completely unbalanced).

  Hence when I do a more in depth assessment of the time complexity of this solution, I can see that the binary search tree is being iterated over a total of two times (once to find the path to v1 and another time to find the path to v2). In addition, at the end of the algorithm, the two path arrays (path1 and path2) are both being iterated over once and in the worst case the v1 and v2 can both point to the same value to a leaf node of a very unbalanced binary tree (meaning that the time complexity of the final while loop can be O(n) as well since in the most extreme case path1 and path2 can mirror the entire length of the binary tree).

  In conclusion the more truthful time complexity assessment of this problem is O(n + n + k) where n is the input and k is the final while loop that is iterating over the path1 and path2 array.

### Space Complexity

- O(n)

- Rationale:

  The rough space complexity assessment of the solution is O(n) since in the worst case (if the binary tree is severely unbalanced) the entirety of the binary tree will need to be appended to the path1 and path2 arrays.

  Due to the nature of the worst case and the fact that there are two arrays that can potentially mirror the entirety of the binary tree the real space complexity is O(n + n).
