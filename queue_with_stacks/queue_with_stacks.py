class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        # stack2 will be the data structure with the correct 
        # variable placement (first in first out)

        # if stack2 is empty move all the elements from 
        # stack1 to stack2

        if len(self.stack2) == 0 and len(self.stack1) > 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) > 0:
            return self.stack2[-1]
        elif len(self.stack2) == 0 and len(self.stack1) == 0:
            return     
        
    def pop(self):
        if len(self.stack2) == 0 and len(self.stack1) > 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
                
        if len(self.stack2) > 0:
            return self.stack2.pop()
        elif len(self.stack2) == 0 and len(self.stack1) == 0:
            return
        
        
    def put(self, value):
        self.stack1.append(value)