class Node:
    def __init__(self, val, current_max):
        self.val = val
        self.prev = None
        self.current_max = current_max

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.largest_val = 0

    def insert(self, val):
        # print('largest value', self.largest_val)
        
        if self.head == None:
            self.head = Node(val, val)
            self.largest_val = val
            # print('largest value node', self.head.current_max)
            # print('node value', self.head.val)
        else:
            # print('largest value node', self.head.current_max)
            # print('node value', val)

            if self.largest_val < val:
                new_head = Node(val, val) 
                new_head.prev = self.head 
                self.head = new_head
                self.largest_val = val
            else:
                new_head = Node(val, self.largest_val) 
                new_head.prev = self.head 
                self.head = new_head
            

    def delete_head(self):
        if self.head:
            if self.head.val == self.largest_val:
                if self.head.prev:
                    self.largest_val = self.head.prev.current_max
                else:
                    self.largest_val = self.head.val
            new_head = self.head.prev
            self.head = new_head

            

            # if self.head != None and self.head.val == self.largest_val[-1]:
            #     self.largest_val.pop()


# stack_list = SingleLinkedList() 
# stack_list.insert(2)
# stack_list.insert(3)
# stack_list.delete_head()


input_data = sys.stdin.readlines()
cleaned_data = []
stack = SingleLinkedList()
for data in input_data[1:]:
    command = data.rstrip().split()
    # cleaned_data.append(new_data)
    if command[0] == '1':
        stack.insert(int(command[1]))
    elif command[0] == '2':
        stack.delete_head()
    elif command[0] == '3':
        print(stack.head.current_max)