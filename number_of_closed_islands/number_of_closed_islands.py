class Solution:
    def closedIsland(self, grid):
        # the best way to solve this problem is through almost the same method 
        # as the island count problem in that I will use a nested for loop to 
        # find the first cell that is an island and use depth first search to 
        # search for all the island cells but if the traversal runs into the borders
        # of the matrix don't count the island as closed. Best way to do this is 
        # to use a unrecousive approach for depth first search 
        
        # first create a count variable 
        # create a visited set() data structure that will carry all the 
        # visited cells 
        
        # create a for loop that will loop through the rows of the matrix 
            # create a for loop that will iterate through each individual 
            # cell 
                # use a depth first search algorithm to traverse through 
                # the grid and save all the traversed island to the visited 
                # set().
                
                
        count = 0 
        visited = set() 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0 and (row, col) not in visited:
                    isEnclosed = self.depth_first_search((row, col), grid, visited)
                    if isEnclosed:
                        count += 1
                        
        return count
                    
    def depth_first_search(self, current_cell, grid, visited):
        # create a stack that will carry all the nodes that need to be explored
        # initialize the stack with the current cell from the arguments 
        # create a variable that will show whether the island is surrounded by 
        # water or not. Initialized to true
        
        # create a while loop that will continue until the stack is empty 
            # pop the tail off the stack 
            
            # add the current node to the visited set() 
            
            # check if current node has land neighbors to the left, right, top, 
            # bottom 
            # place the neighbors in the stack 
            
        stack = [] 
        stack.append(current_cell)
        isEnclosed = True
        
        while len(stack) > 0:
            current_node = stack.pop() 
            visited.add(current_node)
            
            if current_node[0] - 1 == -1 or current_node[0] + 1 == len(grid) or current_node[1] - 1 == -1 or current_node[1] + 1 == len(grid[0]):
                isEnclosed = False
                
            for neighbor in self.find_neighbors(current_node, grid):
                if neighbor not in visited:
                    stack.append(neighbor)
                
        return isEnclosed
            
                
                
    def find_neighbors(self, current_node, grid):
        neighbors = []
        
        if current_node[0] - 1 != -1 and grid[current_node[0]-1][current_node[1]] == 0:
            neighbors.append((current_node[0]-1, current_node[1]))
            
        if current_node[0] + 1 != len(grid) and grid[current_node[0]+1][current_node[1]] == 0:
            neighbors.append((current_node[0]+1, current_node[1]))
            
        if current_node[1] - 1 != -1 and grid[current_node[0]][current_node[1]-1] == 0:
            neighbors.append((current_node[0], current_node[1]-1))
            
        if current_node[1] + 1 != len(grid[0]) and grid[current_node[0]][current_node[1]+1] == 0:
            neighbors.append((current_node[0], current_node[1]+1))
            
        return neighbors 