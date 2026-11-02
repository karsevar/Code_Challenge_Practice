"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # This solution can be regarded as the bruteforce approach where I am going through all the nodes in the 
    # binary tree about two times. The first time to populate the results array in the order of the nodes that 
    # are found in each level and the second time looping through that same results array in order to connect all
    # ajacent nodes. 
    # space complexity can be regarded as O(n) where n are all the nodes in the binary tree
    # time complexity can be regarded as O(n) 
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # for this problem the most straightforward way is to populate a dictionary that contains all the nodes according to their level within the tree. The issue with this approach is how am I going to keep track of the level value. The best way to do this is to bake the level value within the queue or stack element itself. 
        # queue element = {(Optional[Node], level value)}
        # for this first attempt I can use a queue as the primary loop data structure since I will need to keep the explored nodes in order from left to right. 
        # termination conditional will be if the queue is empty and if the left or right node is none it won't enter the queue. 
        # results data structure that the traversal will populate will be dictionary with the level as the key and an array of nodes as the value. 
        # results will look like this {level value: [node, node, ...]}

        # after populating the results map we will need to loop through the resulting map and attach the nodes together from left to right.

        if root == None:
            return None

        queue = [(1, root)]
        results = {}

        while len(queue):
            current_level, current_node = queue[0]
            queue = queue[1:]
            if current_level not in results:
                results[current_level] = [current_node]
            else:
                results[current_level].append(current_node)

            if current_node.left != None:
                queue.append((current_level+1, current_node.left))
            if current_node.right != None:
                queue.append((current_level+1, current_node.right))

        for nodes in results.values():
            for index in range(len(nodes)):
                if index == len(nodes)-1:
                    nodes[index].next = None
                else:
                    nodes[index].next = nodes[index+1]

        return root