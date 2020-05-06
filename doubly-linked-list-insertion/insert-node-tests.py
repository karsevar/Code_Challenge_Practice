import unittest 
from insert_node import sortedInsert, DoublyLinkedListNode


class Test(unittest.TestCase):
    def test_beginning_insertion(self):
        head = DoublyLinkedListNode(1) 
        current_node = head

        for i in range(2, 11):
            new_node = DoublyLinkedListNode(i) 
            current_node.next = new_node 
            new_node.prev = current_node 
            current_node = current_node.next 

        new_head = sortedInsert(head, 1) 
        linkedListArray = []

        current_node = new_head 
        while current_node != None:
            linkedListArray.append(current_node.data)
            current_node = current_node.next 

        self.assertEqual(linkedListArray, [1,1,2,3,4,5,6,7,8,9,10])

    def test_ending_insertion(self):
        head = DoublyLinkedListNode(1) 
        current_node = head

        for i in range(2, 11):
            new_node = DoublyLinkedListNode(i) 
            current_node.next = new_node 
            new_node.prev = current_node 
            current_node = current_node.next 

        new_head = sortedInsert(head, 11) 
        linkedListArray = []

        current_node = new_head 
        while current_node != None:
            linkedListArray.append(current_node.data)
            current_node = current_node.next 

        self.assertEqual(linkedListArray, [1,2,3,4,5,6,7,8,9,10,11])

    def test_middle_insertion(self):
        head = DoublyLinkedListNode(1) 
        current_node = head

        for i in range(2, 11):
            new_node = DoublyLinkedListNode(i) 
            current_node.next = new_node 
            new_node.prev = current_node 
            current_node = current_node.next 

        new_head = sortedInsert(head, 6) 
        linkedListArray = []

        current_node = new_head 
        while current_node != None:
            linkedListArray.append(current_node.data)
            current_node = current_node.next 

        self.assertEqual(linkedListArray, [1,2,3,4,5,6,6,7,8,9,10])

if __name__ == '__main__':
    unittest.main()
