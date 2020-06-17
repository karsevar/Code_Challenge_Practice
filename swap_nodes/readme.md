# Swap Nodes [Algo]

#### 1️⃣ Solution Summary

For my first attempt I literally combined both level order traversal (for the swap nodes logic) and iterative inorder traversal (for returning an array containing the nodes in their respective positions in the binary tree).

As for the tree data structure, I used the passed in indexes array as a substitute since according to the problem's description each index position in the passed in indexes array represents a node and the subarrays under each index position represents the node's children. Below is an example of said structure:

Array representation:

```
indexes = [
    # index 0 node 1:
    [2, 3],
    # index 1 node 2:
    [4, 5],
    # index 2 node 3:
    [-1, -1],
    # index 3 node 4:
    [-1, -1],
    # index 4 node 5:
    [-1, -1]
]
```

Tree representation:

```
              __1__
             /     \
            2       3
           / \
          4   5
```

As you can see -1 can be interpreted as the terminal nodes (or rather nodes that equal null) and in order for the level order traversal algorithm to work I had to minus each node value passed into the queue by one in order to convert the node's value into the actual node's position in the passed in array.

The swap operation was carried out by the swap_nodes function that takes in a query integar argument and uses the modulo operator to decide whether to swap a level's child nodes. It's important to remember that the there are more than one passed in query value and the queries argument passed into the main swapNodes function is actually an array containing integars.

The following is an example of how the swap_nodes function works and is used:

```
queries = [1,2]

query = 1

              __1__     swap
             /     \
            3       2   swap
           / \
          5   4         swap

# Swaps the children of every parent node starting from the first
# level in the binary tree.


query = 2

              __1__
             /     \
            3       2   swap
           / \
          4   5

# Swaps the children of every parent node who's respective level
# is a mulitple of 2.

results in inorder traversal orientation:
4, 3, 5, 1, 2
```

Lastly an iterative inorder traversal algorithm was used in place of the recursive implementation as a means to bypass the recursive depth error that the final two tests in hackerrank were returning.

---

### Technologies Used

- Python

---

## 2️⃣ Challenge Information

| Title             | Challenge URL                                                | Time Complexity | Space Complexity | Difficulty |
| ----------------- | ------------------------------------------------------------ | --------------- | ---------------- | ---------- |
| Swap Nodes [Algo] | https://www.hackerrank.com/challenges/swap-nodes-algo/proble | O(mn)           | O(n)             | Medium     |

## 3️⃣ Time / Space Complexity

### Time Complexity

- O(n)

- Rationale:

  This solution can be defined as having a time complexity of O(n*m), where n is the indexes input (the binary tree in the form of an array with sub-arrays denoting the left and right nodes) and query input (the array containing the swap index queries as integers). The reason for this assessment is that for each integer in the queries array all of the elements in indexes will need to be traversed (checked if the specific node level is a multiple of the query integer). But even with that said, there is an additional O(m*n) operation being performed after the queries for loop. This operation is the inorder_traversal function which needs to traverse through the entire binary tree again to return the inorder orientation of each node after each integer in the queries array.

  In conclusion, the actual time complexity of this algorithm is actually O(mn + mn) but since big O notation is written in short hand the rought estimate is actually O(mn).

### Space Complexity

- O(n)

- Rationale:

  Though misleading the short hand space complexity of this algorithm can be described as O(n). In actuality there are three total data structures that can mirror the same size as the binary tree in the worst case (which are the stack data structure in the inorder_traversal function, queue data structure in the swap_nodes function, and lastly the solution_string array that holds the inorder traversal results of the inorder_traversal function). In both the best and worst case the solution_string array will allows mirror the total number of nodes in the passed in binary tree while one can't be certain of the inherent size of the queue and stack as they both tend to increase and descrease in runtime.

  Hence if one assumes that the solution_string array is the only data structure that mirrors the total number of nodes in the passed in binary tree at any given moment the rough space complexity is O(n)
