# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time complexity is O(v) and space complexity is O(v)
    def maxLevelSum(self, root: TreeNode | None) -> int:
        # okay so the most straightforward way to solve this is to traverse through the binary search tree and document the specific level of each node and increment the level value when adding a neighboring node to the queue. We can either do breadth first search or depth first search.

        # we will need to create a visited set that will keep track of the already visited tree nodes.
        # we will need to create another array that will keep track of the node value with their level in the binary tree so that we can compose the sums

        queue = [] # [(level, treenode), (level, treenode)]
        level_values = {} # {level: [treenode.val, treenode.val]}
        visited = set() # set[treenode]

        if root == None:
            return 0

        queue.append((1, root))

        while len(queue):
            currentLevel, currentNode = queue[0]
            queue = queue[1:]

            if currentLevel not in level_values:
                level_values[currentLevel] = currentNode.val
            else:
                level_values[currentLevel] += currentNode.val

            if currentNode.left:
                queue.append((currentLevel+1, currentNode.left))

            if currentNode.right:
                queue.append((currentLevel+1, currentNode.right))
                
        highestLevel = (1, level_values[1])

        for level, levelValue in level_values.items():
            if highestLevel[1] < levelValue:
                highestLevel = (level, levelValue)

        return highestLevel[0]