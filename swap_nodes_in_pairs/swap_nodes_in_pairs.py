class Solution:
    def swapPairs(self, head):
        # create a check condition that will see if the input linked list 
        # is one node long or is empty 
            # if so return the head 
        # if not 
            # create a current node variable 
            
            # since the problem says that I should only swap pairs 
            # there should be a condition where if the current node's 
            # next node is null don't do anothing 
            
            # create a while loop that will loop through the linked list
            # terminating if the current node's next node is null 
                # create a new variable that will hold the next node 
                # add the current node to the next node of the new variable 
            
        if head == None:
            return head 
        elif head.next == None:
            return head
        else:
            new_head = head.next 
            future_node = new_head.next 
                
            new_head.next = head 
            head.next = future_node
            
            past_node = head
            current_node = future_node
            
            while current_node != None and current_node.next != None:
                next_node = current_node.next 
                future_node = next_node.next 
                
                next_node.next = current_node
                past_node.next = next_node
                current_node.next = future_node
                
                past_node = current_node
                current_node = future_node 
                
            return new_head