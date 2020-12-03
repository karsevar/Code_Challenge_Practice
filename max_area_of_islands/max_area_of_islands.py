class Solution:
    def maxAreaOfIsland(self, grid):
        # it seems that this problem is a combination of two other problems 
        # the island counting problem and the perimeter counting problem 
        # the main issue with combining these two solutions is that the time 
        # complexity might be inefficient.
        
        visited = set() 
        max_count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if grid[row][col] == 1:
                #     print('position of island cell', (row, col))
                if (row, col) not in visited and grid[row][col] == 1:
                    count = self.depth_first_search((row, col), grid, visited)
                    
                    if max_count < count:
                        max_count = count
                        
        return max_count
                    
    def depth_first_search(self, current_cell, grid, visited):
        stack = []
        stack.append(current_cell) 
        edges = 0
        
        print('---- new depth first search instance ----')
        while len(stack) > 0:
            # print('current stack', stack)
            current_node = stack.pop() 
            # print('current node', current_node)
            neighbors = self.find_neighbors(current_node, grid, visited)
            # print('neighbors', neighbors[1])
            
            if current_node not in visited:
                edges += 1
                
            print('edge count', edges)
                
            visited.add(current_node)
                
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
        return edges
                
                
    def find_neighbors(self, current_cell, grid, visited):
        row = current_cell[0]
        col = current_cell[1]
        # print('row and col', (row, col))
        # print('current cell in neighbors', current_cell)
        neighbors = []
        
        if row-1 != -1 and grid[row-1][col] == 1:
            neighbors.append((row-1, col))
            # print('found top node', (row-1, col))
            
        if row+1 != len(grid) and grid[row+1][col] == 1:
            neighbors.append((row+1, col))
            # print('found bottom node', (row+1, col))
            
        if col-1 != -1 and grid[row][col-1] == 1:
            neighbors.append((row, col-1))
            # print('found left node', (row, col-1))
            
        if col+1 != len(grid[0]) and grid[row][col+1] == 1:
            neighbors.append((row, col+1))
            # print('found right node', (row, col+1))
            
        return neighbors