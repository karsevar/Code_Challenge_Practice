class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # First get the intersection point through having two pointers 
        # go through the algorithm 
            # one iterating through the linked list by two nodes and 
            # the other iterating through the linked list by one node 
            
            # if an intersection point is found return the intersection point 
            
        # create an additional for loop that will run from the head node to 
        # the intersection node, documenting the number of nodes it steps through 
        # before the intersection node
        
        slow_pointer = head 
        
        if head == None:
            return None
        elif head.next == None:
            return None
        elif head.next.next == None:
            return None 
        else:
            fast_pointer = head
            intersection = None
        
        while slow_pointer != None or fast_pointer != None:
            
            if fast_pointer.next == None:
                return None
            if fast_pointer.next.next == None:
                return None
            
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next
            
            if slow_pointer == fast_pointer:
                intersection = slow_pointer 
                break
            
        pointer1 = head 
        pointer2 = intersection 
            
        while pointer1 != pointer2:
            pointer1 = pointer1.next 
            pointer2 = pointer2.next
            
            
        return pointer1