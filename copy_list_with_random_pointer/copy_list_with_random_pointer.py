"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # The conditionals are a little rough with this implementation but the time complexity can be regarded as 
    # adequate since we are only looping through the linked list once.
    # time complexity is O(n)
    # space complexity is O(n) since the clones dictionary will contain all the nodes within the linked list.
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # I think I can use the same method as the last problem where I simply create a clones dictionary mapping the old node to the new node

        # initialize a stack and add the head to the stack
        # I think we don't really need a visited set since the linked list is only going in one direction and I'm only using the next attribute to traverse the map.

        # create a while loop that will terminate once the stack length reaches zero
        
        if head == None:
            return None

        clones = {
            head: Node(head.val)
        }
        current_node = head

        while current_node:
            cloned_node = clones[current_node]
            next_node = current_node.next

            if next_node != None and next_node not in clones:
                clones[next_node] = Node(next_node.val)
                cloned_node.next = clones[next_node]
            elif next_node != None and next_node in clones:
                cloned_node.next = clones[next_node]
            elif next_node == None:
                cloned_node.next = None

            random_node = current_node.random
            if random_node != None and random_node not in clones:
                clones[random_node] = Node(random_node.val)
                cloned_node.random = clones[random_node]
            elif random_node != None and random_node in clones:
                cloned_node.random = clones[random_node]
            elif random_node == None:
                cloned_node.random = None

            current_node = next_node

        return clones[head]