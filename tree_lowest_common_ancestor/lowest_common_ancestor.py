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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here

  # My first attempt approach will be running breadth first search on v1 and v2
  # and having the two algorithm runs return a path variable that is a list 
  # of all the nodes traversed to get to the specific value in the binary tree  
  
  # create a helper function that will be used for breadth first search functionality
  # arguments target node value root node
    # create a queue 
    # initialize the queue with an array that has the root node

    # create a while loop that will terminate once queue is empty 
        # pop head off of queue 

        # check if head array node has the same value as target value
        # if so return head array 
        # if not:
            # if head array node value is less than target value 
                # add left node to the queue 
            # if head array node value is greater than target value 
                # add right node to the queue 

    def breadth_search_helper(root, target):
        queue = []
        queue.append([root])

        while len(queue) > 0:
            path = queue.pop(0)

            if path[-1].info == target:
                return path 

            else:
                if path[-1].info > target:
                    new_path = list(path) 
                    new_path.append(path[-1].left)
                    queue.append(new_path)
                else:
                    new_path = list(path) 
                    new_path.append(path[-1].right)
                    queue.append(new_path)

    path1 = breadth_search_helper(root, v1)
    path2 = breadth_search_helper(root, v2)

    index = 0
    solution_pointer = None

    if path1[0].info == v1:
        return path1[0]
    elif path2[0].info == v2:
        return path2[0]

    while True:
        if len(path1) == index:
            return solution_pointer 
        elif len(path2) == index:
            return solution_pointer
        if path1[index] == path2[index]:
            solution_pointer = path1[index]
            index += 1
        else:
            return solution_pointer

array = [8,4,9,1,2,3,6,5]
tree = BinarySearchTree()
tree.create(array[0])

for value in array[1:]:
    tree.create(value)


node = lca(tree.root, 1,2)
print(node.info)
