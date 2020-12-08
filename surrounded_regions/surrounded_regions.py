class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        # solve this problem the same way that I solved the islands problem
        
        # create a visited set that will carry the tuples of all the visited cells 
        # in the grid 
        
        # create a for loop that will loop through the rows of the grid 
            # create a for loop that will loop through the cols of the grid 
                # check if the current cell is equal to 0 
                    # if yes use the current cell as the starting point to 
                    # traverse the grid 
                    
        visited = set() 
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and (row, col) not in visited:
                    visited.update(self.depth_traversal(row, col, board))
                    
                    
    def depth_traversal(self, row, col, board):
        # create a queue that will be initialized with the (row, col) arguments passed
        # into the depth_traversal function 
        
        # create checked_spots set that will be used to convert all the O to X if 
        # the island is enclosed
        
        # create an isEnclosed boolean initialized to True
        
        
        # create a while loop that will terminate once the queue is empty 
            # pop the tail off of the queue 
            # add the current node to the checked_spots set 
            
            # find the neighbors of the current cell
                # check if the neighboring cell is O and not a boundary cell 
                    # if yes add the neighbors to the queue 
                    # if not change the isEnclosed boolean to False
                    
        queue = []
        checked_spots = set()
        isEnclosed = True
        
        queue.append((row, col)) 
        
        while len(queue) > 0:
            (cur_row, cur_col) = queue.pop() 
            checked_spots.add((cur_row, cur_col))
            
            for (next_row, next_col) in [(cur_row-1, cur_col), (cur_row+1, cur_col), (cur_row, cur_col-1), (cur_row, cur_col+1)]:
                if next_row != -1 and next_row != len(board) and next_col != -1 and next_col != len(board[0]):
                    if board[next_row][next_col] == 'O' and (next_row, next_col) not in checked_spots:
                        queue.append((next_row, next_col))
                else:
                    isEnclosed = False 
                    
        # print('checked_spots', checked_spots)
        if isEnclosed:
            for cell in checked_spots:
                board[cell[0]][cell[1]] = 'X'
                    
        return checked_spots