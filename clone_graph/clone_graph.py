"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
# This isn't really the cleanest and best solution as I'm traversing through the graph two times and I'm also 
# populating two datastructures that grow to the same size as the number of nodes in the graph.

# The simple time complexity of this solution can be conceptualized as O(n*2) where I'm traversing through the graph
# two separate times and the space complexity is O(n*2) as well due to the two datastructures that I'm using to save the 
# addresses of the new nodes and ensure that I don't reprecess the old nodes.
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Okay I believe that we can use simple depth first search for this problem through simply creating a stack populated by all the neighbors in which the first node and succeeding nodes are connected to.

        # The graph in undirected so we will need to keep track of a visited node. The main issue that I can think of is how to copy each node into their own new node. 

        # I think I can use the val field to my advantage since they all coorespond to their index position. I can use this as a means to design a dictionary where the val field acts as the key and the value will be the new node value.

        # so we will have to initialize a visited set that will keep track of all the nodes that we visited in the old graph.
        # we will need to initialize a dictionary that will keep track of all the new nodes that we created with their cooresponding new node signatures.
        # newNodes = {val: new_node signature}

        # initialize a stack array that will start with the passed in node

        # create a while loop that will terminate when stack is empty
        # pop node from stack
        # create a copy of current node
        # add copy of current node to the newNodes dictionary newNodes[val] = copy of current Node
        # loop through neighbors list
        # if neighbor is not in visited set
        # add neighbor to the stack

        if node == None:
            return None
        stack = [node]
        newNodes = {}
        visited = set()
        visited.add(node)

        while len(stack) > 0:
            current_node = stack.pop()
            newNodes[current_node.val] = Node(current_node.val)

            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        stack = [node]
        visited = set()
        visited.add(node)

        while len(stack):
            current_node = stack.pop()
            copied_node = newNodes[current_node.val]

            for neighbor in current_node.neighbors:
                copied_node.neighbors.append(newNodes[neighbor.val])
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return newNodes[1]