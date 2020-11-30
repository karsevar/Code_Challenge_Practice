class Solution:
    def numIslands(self, grid):
        # brady solved this problem through first having a for loop that 
        # will loop through each individual cell in the matrix 
        # and in the middle of the nested for loop he ran a depth 
        # first search algorithm to find all the connected cells 
        # of the island 
        
        # first create a counts variable 
        # create a visited set that will remember all the cells in (row, col)
        # format 
        
        # create a nested for loop that starts at the first row 
            # create a for loop that will start at the first column 
                # check if current cell is 1 and not in visited 
                    # create a depth first search algorithm that will 
                    # fill out visited array with all the traversed cells
                    
        count = 0 
        visited = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    visited.add((row, col))
                    count += 1
                    self.depth_first_search((row, col), visited, grid)
                    
        return count
        
    def depth_first_search(self, root_cell, visited, grid):
        # create a depth first search function that will traverse through the matrix 
        # and add all the unvisited cells connected to the root_cell to visited set().
        
        # create recursion helper function that will carry all the depth first 
        # algorithm logic 
        
        def recursion_helper(current_cell, visited, grid):
            if current_cell != None:
                visited.add(current_cell)
                for neighbor in self.find_neighbors(current_cell, grid):
                    if neighbor not in visited:
                        recursion_helper(neighbor, visited, grid)
                
                
        recursion_helper(root_cell, visited, grid)
            
    def find_neighbors(self, current_cell, grid):
        neighbors = []
        if current_cell[0] - 1 != -1 and grid[current_cell[0]-1][current_cell[1]] == '1':
            neighbors.append((current_cell[0]-1, current_cell[1]))
        if current_cell[0] + 1 != len(grid) and grid[current_cell[0]+1][current_cell[1]] == '1':
            neighbors.append((current_cell[0]+1, current_cell[1]))
        if current_cell[1] - 1 != -1 and grid[current_cell[0]][current_cell[1] - 1] == '1':
            neighbors.append((current_cell[0], current_cell[1]-1))
        if current_cell[1] + 1 != len(grid[0]) and grid[current_cell[0]][current_cell[1]+1] == '1':
            neighbors.append((current_cell[0], current_cell[1]+1))
            
        return neighbors