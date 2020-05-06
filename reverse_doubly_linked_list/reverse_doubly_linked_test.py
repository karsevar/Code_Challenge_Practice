import unittest 
from reverse_doubly_linked import DoublyLinkedListNode, reverse

class Test(unittest.TestCase):
    def reverse_small_linked_list(self):
        head = DoublyLinkedListNode(1) 
        current_node = head 

        for i in range(2, 11):
            new_node = DoublyLinkedListNode(i) 
            current_node.next = new_node 
            new_node.prev = current_node 
            current_node = current_node.next 

        new_head = reverse(head) 

        linkedListArray = []
        current_node = new_head 

        while current_node != None:
            linkedListArray.append(current_node.data)
            current_node = current_node.next 

        self.assertEqual(linkedListArray, [i for i in range(10, 0, -1)])

    def reverse_medium_linked_list(self):
        head = DoublyLinkedListNode(1) 
        current_node = head 

        for i in range(2, 300):
            new_node = DoublyLinkedListNode(i) 
            current_node.next = new_node 
            new_node.prev = current_node 
            current_node = current_node.next 

        new_head = reverse(head) 

        linkedListArray = []
        current_node = new_head 

        while current_node != None:
            linkedListArray.append(current_node.data)
            current_node = current_node.next 

        self.assertEqual(linkedListArray, [i for i in range(300, 0, -1)])

    def reverse_large_linked_list(self):
        head = DoublyLinkedListNode(1) 
        current_node = head 

        for i in range(2, 10000):
            new_node = DoublyLinkedListNode(i) 
            current_node.next = new_node 
            new_node.prev = current_node 
            current_node = current_node.next 

        new_head = reverse(head) 

        linkedListArray = []
        current_node = new_head 

        while current_node != None:
            linkedListArray.append(current_node.data)
            current_node = current_node.next 

        self.assertEqual(linkedListArray, [i for i in range(10000, 0, -1)])

if __name__ == '__main__':
    unittest.main()