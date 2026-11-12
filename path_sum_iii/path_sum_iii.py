# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth first search with backtracking.
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        results = set()
        return self.recursionHelper(root, [], targetSum)


    def recursionHelper(self, root: TreeNode | None, currentPath: list[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0 
        
        currentPath.append(root.val)

        pathCount = 0
        currentSum = 0

        for i in range(len(currentPath) - 1, -1, -1):
            currentSum += currentPath[i]

            if currentSum == targetSum:
                pathCount += 1

        pathCount += self.recursionHelper(
            root.left, currentPath, targetSum
        )

        pathCount += self.recursionHelper(
            root.right, currentPath, targetSum
        )

        currentPath.pop()

        return pathCount