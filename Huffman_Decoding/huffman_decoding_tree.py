import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()

    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    
    # Convert the s input into a queue since strings are immutable 
    # initialize results string
    
    # create a while loop that will terminate once the queue is 
    # empty 
        # initialize the current_node to the root node 

        # create an additional while loop that will terminate 
        # once a terminal node is found 
    
            # if current_node.left and current_node.right are None
                # concatenate current_node.data to the result string 
                # break

            # else:
                # pop head value off queue 
                # if head value is 0 increment current_node.left 
                # if head value is 1 increment current_node.right

    queue = list(s)
    results_string = ''
    
    while len(queue) > 0:
        current_node = root 
        while True:
            if current_node.left == None and current_node.right == None:
                # print(queue)
                # print('hello terminal node', current_node.data)
                results_string += current_node.data
                break

            elif current_node.right != None or current_node.left != None:
                direction = queue.pop(0)
                if direction == '0':
                    current_node = current_node.left
                else:
                    current_node = current_node.right

    print(results_string)