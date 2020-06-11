# Swap Nodes [Algo]

#### 1️⃣ Solution Summary

For my first attempt solution I used breadth first search to find the respective paths from the root node to the values assigned to the variables v1 and v2. Ultimately I iterated over the binary tree two different times to find the traversal paths to the variables v1 and v2. The traversal paths are both arrays (containing the node pointers from the root to the target node). After the breadth first search steps I compared the two path arrays and return the last matching pointer node between to two path arrays.

---

### Technologies Used

- Python

---

## 2️⃣ Challenge Information

| Title             | Challenge URL                                                | Time Complexity | Space Complexity | Difficulty |
| ----------------- | ------------------------------------------------------------ | --------------- | ---------------- | ---------- |
| Swap Nodes [Algo] | https://www.hackerrank.com/challenges/swap-nodes-algo/proble | O(n)            | O(n)             | Medium     |

## 3️⃣ Time / Space Complexity

### Time Complexity

- O(n)

- Rationale:

### Space Complexity

- O(n)

- Rationale:

  Though misleading the short hand space complexity of this algorithm can be described as O(n). In actuality there are three total data structures that can mirror the same size as the binary tree in the worst case (which are the stack data structure in the inorder_traversal function, queue data structure in the swap_nodes function, and lastly the solution_string array that holds the inorder traversal results of the inorder_traversal function). In both the best and worst case the solution_string array will allows mirror the total number of nodes in the passed in binary tree while one can't be certain of the inherent size of the queue and stack as they both tend to increase and descrease in runtime.

  Hence if one assumes that the solution_string array is the only data structure that mirrors the total number of nodes in the passed in binary tree at any given moment the rough space complexity is O(n)
