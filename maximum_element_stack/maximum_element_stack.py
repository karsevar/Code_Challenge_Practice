# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# first create a singly linked list class this will be the base data structure 
# used for this problem (the stack)

# first create a node class that will only have a marker to the next node 
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.largest_val = None

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
            self.largest_val = val
        else:

            if self.largest_val < val:
                new_head = Node((2*val) - self.largest_val) 
                new_head.prev = self.head 
                self.head = new_head
                self.largest_val = val
            else:
                new_head = Node(val) 
                new_head.prev = self.head 
                self.head = new_head
            

    def delete_head(self):
        if self.head:
            new_head = self.head.prev
            self.head = new_head

            if new_head != None and new_head.val > self.largest_val:
                self.largest_val = (2*self.largest_val) - new_head.val

            # if self.head != None and self.head.val == self.largest_val[-1]:
            #     self.largest_val.pop()


# stack_list = SingleLinkedList() 
# stack_list.insert(2)
# stack_list.insert(3)
# stack_list.delete_head()


input_data = sys.stdin.readlines()
cleaned_data = []
for data in input_data:
    new_data = data.rstrip().split()
    cleaned_data.append(new_data)

# create a command flow 
# loop through the cleaned_data array (ignoring of course the first index) 
    # if the first index in cleaned_data[i] is 1 
        # insert the second index value into the SingleLinkedList 
    # elif the first index in cleaned_data[i] is 2 
        # delete the head node of the singlelinked list
    # elif the first index in cleaned_data[i] is 3
        # iterate through the singlelinkedlist and find the largest value in the 
        # list 

stack = SingleLinkedList()
for command in cleaned_data[1:]:
    if command[0] == '1':
        stack.insert(int(command[1]))
    elif command[0] == '2':
        stack.delete_head()
    elif command[0] == '3':
        print(stack.largest_val)