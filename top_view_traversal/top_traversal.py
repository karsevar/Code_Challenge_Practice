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
    hashtable[0] = set()
    hashtable[0].add(str(root.info))
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
                hashtable[leftHd] = set()
            hashtable[leftHd].add(str(current_node.left.info))
            queue.append(current_node.left)

        if current_node.right != None:
            rightHd = Hd + 1
            if rightHd not in hashtable:
                hashtable[rightHd] = set()
            hashtable[rightHd].add(str(current_node.right.info))
            queue.append(current_node.right)
    
    string_variable = ''
    print(hashtable)
    print(level_array)
    keys = list(hashtable.keys())
    keys.sort()
    for key in keys:
        if len(hashtable[key]) > 1:
            lowest_index = float('inf')
            for sub_key in hashtable[key]:
                print('sub key', sub_key)
                for index in range(len(level_array)):
                    if str(level_array[index]) == sub_key:
                        if lowest_index > index:
                            lowest_index = index
            lowest_index = int(lowest_index)

            string_variable += str(level_array[lowest_index]) + ' '

        else:
            string_variable += hashtable[key].pop() + ' '

    print(string_variable)

tree = BinarySearchTree()

test_array = [37, 23, 108, 59, 86, 64, 94, 14, 105, 17, 111 ,65 ,55, 31, 79, 97, 78 ,25, 50, 22 ,66 ,46, 104, 98 ,81, 90, 68, 40 ,103, 77, 74, 18, 69, 82 ,41, 4 ,48 ]
tree.create(test_array[0])

for value in test_array[1:]:
    tree.create(value)

topView(tree.root)



# 37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 1