# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # This is not really the most optimal solution as I'm looping through every node in the tree structure.
    # and within that loop I'm copying the path state and then checking if the sum lines up with targetSum.
    # The time complexity of this solution at there for me regarded as O(n^2) where n is the number of nodes in the tree structure. This is because for every node in the tree structure we are copying the state of the path and then checking if the sum lines up with targetSum.
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # okay for this problem I will need to have a results array that will keep track of all the possible paths that lead to the target sum as well as the state of the current recursive loop.

        results = []

        self.recursive_helper(
            [],
            root,
            targetSum, 
            results
        )

        return results

    def recursive_helper(self, state: List[int], treeNode: Optional[TreeNode], targetSum: int, results: List[List[int]]):
        # create a conditional that will check if the sum of state equals the target sum
        # if it does than we can add the copy of the state to the results array

        # create a conditional that check if the current node is a treeNode or null
        # if a treeNode 
        # add current node value to state
        # recursively call the function on the right and left nodes

        if treeNode != None and treeNode.left == None and treeNode.right == None:
            result_state = [*state, treeNode.val]
            if len(result_state) != 0 and sum(result_state) == targetSum:
                results.append(result_state)

        if treeNode != None:
            if treeNode.left:
                self.recursive_helper([*state, treeNode.val], treeNode.left, targetSum, results)
            if treeNode.right:
                self.recursive_helper([*state, treeNode.val], treeNode.right, targetSum, results)


class SolutionBackTracking:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # the most straightforward way is to use recursion and backtracking with the same principles as depth first search. 

        # the base case for the recursive function will be if the current node is null (this means that we reached the end of the tree) and the current sum is equal to the target sum. If these conditions are met than we can add the path values to the outgoing results array. 
        # This problem is a little more simpler than initially thought since we only need to calculate the sum from the root node to a leaf node that lives either to the right or to the left.

        results = []
        if root:
            self.recursion_helper(
                root,
                0,
                targetSum,
                [],
                results,
            )
        return results




    def recursion_helper(self, root: Optional[TreeNode], currentSum: int, targetSum: int, state: List[int], results: List[List[int]]):
        if root is None:
            return 

        state.append(root.val)
        currentSum += root.val

        if root.left == None and root.right == None:
            if currentSum == targetSum:
                results.append(state.copy())

        else:
            self.recursion_helper(
                root.left,
                currentSum,
                targetSum,
                state,
                results,
            )
            self.recursion_helper(
                root.right,
                currentSum,
                targetSum,
                state,
                results,
            )
        state.pop()