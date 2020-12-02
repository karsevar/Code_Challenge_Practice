class Solution:
    def islandPerimeter(self, grid):
        # it seems that I don't have to worry about the edge case 
        # of there being water within the island thus messing with the 
        # parameter count. 
        
        # best way to solve this problem is to first create a nested for loop 
        # that will find the nearest island node and after that use depth first 
        # search to traverse through all the island nodes that make up the one 
        # island. The parameter is found through the find_neighbors function that 
        # increments the edges counter of a specific cell if the cell is surrounded 
        # by water the edges will be 4.
         
        visited = set()
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    # print('found island node', grid[row][col])
                    count = self.depth_first_search((row, col), visited, grid)
                    break
                    
        return count
                    
        
                    
    def depth_first_search(self, current_cell, visited, grid):
        stack = []
        stack.append(current_cell)
        count = 0
        
        while len(stack) > 0:
            current_node = stack.pop() 
            
            neighbors = self.find_neighbors(current_node, visited, grid)
            if current_node not in visited:
                count += neighbors[0]
                
            visited.add(current_node)
            
            for neighbor in neighbors[1]:
                if neighbor not in visited:
                    stack.append(neighbor)
                
        return count
                
            
            
            
    def find_neighbors(self, current_cell, visited, grid):
        row = current_cell[0]
        col = current_cell[1]
        
        neighbors = []
        edges = 4
        
        if row-1 != -1 and grid[row-1][col] == 1:
            neighbors.append((row-1, col))
            edges -= 1
            
        if row+1 != len(grid) and grid[row+1][col] == 1:
            neighbors.append((row+1, col))
            edges -= 1
            
        if col-1 != -1 and grid[row][col-1] == 1:
            neighbors.append((row, col-1))
            edges -= 1
            
        if col+1 != len(grid[0]) and grid[row][col+1] == 1:
            neighbors.append((row, col+1))
            edges -= 1
            
        return (edges, neighbors)