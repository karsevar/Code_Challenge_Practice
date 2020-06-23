
def isPalindrome(head):
        
        # first create a slow node pointer
        # create a fast node pointer
        
        # create a stack that will contain all the values traversed by the slow 
        # node 
        
        # create a while loop that will continue until the fast node is none or 
        # the next node of the fast node is none 
            # push value in slow node to stack 
            # increment slow node by one node 
            # increment fast node by two nodes 
            
        # if the fast node pointer is not none increment slow node by one 
        
        # create another while loop that will have the slow node iterate over the 
        # remainder of the list
            # pop the head of the stack if the head of the stack is not equal 
            # to the current node value return false 
            
    slow = head 
    fast = head
    stack = []
        
    while fast != None and fast.next != None:
        stack.append(slow.val)
        fast = fast.next.next 
        slow = slow.next 
            
    if fast != None:
        slow = slow.next 
            
    while slow != None:
        if (stack.pop() != slow.val):
            return False 
        slow = slow.next 
            
    return True
        