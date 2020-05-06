class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data 
        self.prev = None 
        self.next = None

def sortedInsert(head, data):
    # create a variable called current_node 
    # initialize current_node to the head node 

    # create a while loop that will terminate once current_node is none 
        # check if the data in current node is more than data 
        # if so:
            # make a new doubly linked node with the passed in data 
            # overwrite the next and prev attributes with current_node.next and 
            # current_node.prev respectively 

            # overwrite the next node of the previous node reference with the new node
            # overwrite the past node of the current_node with the new node 

        # else:
            # increment current_node to the next node 

    current_node = head

    while current_node != None:
        # check if the current_node has a next node
        # if not it means that we are adding the new node to the 
        # end of the linked list 
        # check if the current_node has a prev node if not 
        # it means that we are adding the new node to the 
        # start of the linked list 
        new_node = DoublyLinkedListNode(data)
        if current_node.data >= data:
            if current_node.prev == None:
                new_node.next = current_node
                current_node.prev = new_node
                return new_node
            else:
                new_node.prev = current_node.prev 
                new_node.next = current_node 
                current_node.prev.next = new_node 
                current_node.prev = new_node 
                break
        elif current_node.next == None:
            current_node.next = new_node
            new_node.prev = current_node 
            break

        else:
            current_node = current_node.next

    return head