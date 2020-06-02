## Vertical Order Traversal 

# Algorithm - level order traversal and hash table 
# 1.) Enqueue root 
# 2.) Update Hd for root 
# 3.) Add Hd = 0 in Hash table and root as the value
# 4.) Dequeue and 
        # 1 check for left and right child and update 
        # Vd in hashtable 
        # 2 Enqueue the left and right children 

## hash table example:
# hashtable = {
#     horizontal distance: {nodes}
# }

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

alpha_array = ['f','a','b','c','d','e','g','h','i','j','k','l','m']
tree = BinarySearchTree()
tree.create(alpha_array[0])
for alpha in alpha_array[1:]:
    tree.create(alpha)

def vertical_order_traversal(root):
    queue = []
    hashtable = {}

    # initialize the algorithm through enqueuing 
    queue.append(root)

    # update the hashtable with the horizontal distance
    # of the root node 
    hashtable[0] = set(root.info)

    while len(queue) > 0:
        current_node = queue.pop(0) 

        # find the horizontal distance associated with 
        # the current node

        Hd = 0 
        for key in hashtable:
            if current_node.info in hashtable[key]:
                Hd = key

        print(Hd)

        if current_node.left != None:
            Hd -= 1 
            if Hd not in hashtable:
                hashtable[Hd] = set(current_node.left.info)
            else:
                hashtable[Hd].add(current_node.left.info)

            queue.append(current_node.left)

        if current_node.right != None:
            Hd += 1
            if Hd not in hashtable:
                hashtable[Hd] = set(current_node.right.info)
            else:
                hashtable[Hd].add(current_node.right.info)

            queue.append(current_node.right)

    return hashtable 

print(vertical_order_traversal(tree.root))





