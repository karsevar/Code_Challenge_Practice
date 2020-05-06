class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None 
        self.next = None 

def reverse(head):
    # recursive solution much like that of the singly 
    # linked list reverse function.


    # create a recursion helper function that will take in an argument called 
    # current_node 
        # if head.next is None this means the function has 
        # recursed to the end of the linked list 
            # overwrite the globally defined head node with the 
            # last node in the linked list 

            # overwrite the next node with the previous node 
            # overwrite the previous node with the next node 

        # else 
            # recursively call the helper function with the next node 
            # overwrite the next node with the previous node 
            # overwrite the previous node with the next node 

    def recursion_helper(current_node):
        if current_node.next == None:
            new_head = current_node 
            new_next = current_node.prev 
            new_previous = current_node.next 
            new_head.next = new_next 
            new_head.prev = new_previous
            return new_head

        else:
            new_head = recursion_helper(current_node.next)
            new_next = current_node.prev 
            new_prev = current_node.next 
            current_node.next = new_next 
            current_node.prev = new_prev
            return new_head

    # print(recursion_helper(head).next.next.data)
    # print('new head node', new_head)
    return recursion_helper(head) 