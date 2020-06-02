class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    
    # first carry out level order traversal
    # create a queue 
    # initialize the queue with the root node
    # create a level order array 

    # create a while loop that will terminate once the queue is 
    # empty 
        # dequeue the head node 
        # add node to level order array
        # if current_node has a left node add left node to queue 
        # if current_node has a right node add right node to queue 
        
    queue = []
    queue.append(root)
    level_array = []

    while len(queue) > 0:
        current_node = queue.pop(0) 
        level_array.append(current_node.info)

        if current_node.left != None:
            queue.append(current_node.left)

        if current_node.right != None:
            queue.append(current_node.right)

    queue = []
    hashtable = {}
    hashtable[0] = set(str(root.info))
    queue.append(root)
    
    while len(queue) > 0:
        current_node = queue.pop(0) 

        Hd = 0 
        for key in hashtable:
            if str(current_node.info) in hashtable[key]:
                Hd = key 
        
        if current_node.left != None:
            leftHd = Hd - 1
            if leftHd not in hashtable:
                hashtable[leftHd] = set(str(current_node.left.info))
            else:
                hashtable[leftHd].add(str(current_node.left.info))
            queue.append(current_node.left)

        if current_node.right != None:
            rightHd = Hd + 1
            if rightHd not in hashtable:
                hashtable[rightHd] = set(str(current_node.right.info))
            else:
                hashtable[rightHd].add(str(current_node.right.info))
            queue.append(current_node.right)

    print(level_array)
    print(hashtable)