class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create an over arching while loop that will terminate once k reaches 0. K will be decrimented by one with each iteration of this overarching loop.

            # create an additional loop that will terminate once the last node is reached. Keep in mind that a pointer will need to be used to keep track of the previous node.
            # set the next attribute of the second to last node to None
            # set the tail nodes next attribute to current head 
            # set tail node as the new head node

        # decriment k variable by one

        # return head

        ## It seems that this brute force solution will only work for 12 of the 232 usecases. Will need to think of a way to cut down the time complexity. Perhaps we can cut down the time complexity through dividing the number of permutations that are required by the number of nodes in the list. Though I don't really know if this will cut down the time complexity by much.

        ## Perhaps we can have two separate while loops one that gets the pointers for the second to last and last nodes and have the other just simply rotate the nodes k number of times. 

        if head == None:
            return head

        if head.next == None:
            return head

        

        while k != 0:
            previous_node = head
            tail_node = head.next
            while tail_node.next != None:
                previous_node = tail_node
                tail_node = tail_node.next

            tail_node.next = head
            previous_node.next = None

            head = tail_node
            

            k -= 1

        return head
    
    def rotateRightAccepted(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        print("k//length: ", k%length)

        k = length - (k%length)
        
        print("k: ", k)
        while k>0:
            print("k increment: ", k)
            cur = cur.next
            k-=1

        newhead = cur.next
        cur.next=None
        return newhead