class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.

        # check if self.root is None 
        # if yes:
            # create a new node class with the passed
            # in value 
            # overwrite self.root with the newly created node 

        # if not:
            # create a current_node variable that holds the current
            # node 

            # create a while loop that will terminate once 
            # the new node is inserted 
                # if val is greater than current_node.info 
                    # check if current_node.right is None 
                        # if so insert node to current_node.right 
                        # break loop 
                    # else 
                        # iterate the current_node.right 

                # if val is lower than current_node.info
                    # check if current_node.left is None 
                        # if so insert node to current_node.left 
                    # else 
                        # iterate to current_node.left 

        if self.root == None:
            self.root = Node(val) 
        else:
            current_node = self.root 

            while True:
                if current_node.info > val:
                    if current_node.left == None:
                        current_node.left = Node(val)
                        break
                    else:
                        current_node = current_node.left 

                else:
                    if current_node.right == None:
                        current_node.right = Node(val)
                        break
                    else:
                        current_node = current_node.right