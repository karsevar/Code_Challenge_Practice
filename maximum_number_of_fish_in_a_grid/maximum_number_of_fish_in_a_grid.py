class Solution:
    # Breadth first search solution where the time complexity can be conceptualized as O(n*m) since we are 
    # going through all the cells within the 2D matrix at least once thanks to the visited set. The outer 
    # nested for loops is iterating through each cell just to find a possible entry point to explore. And the 
    # inner breadth first search loop is iterating all nearby cells that fit a specific criteria.

    # Space complexity is O(n*m) since in the worst case visited set can contain all the cells in the matrix
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # This is another breadth first search problem where I will have to iterate through the 2X matrix cell by cell until I reach a none 0 cell. Each none zero cell I will need to iterate the count value by the number in the cell and move to the cell's neighbor in the four immediate directions up, down, left, or right. We will need to keep track of all the cells that have already been visited as a means to not double count fish.

        max_count = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i, j) not in visited:
                    visited.add((i, j))
                    current_count = grid[i][j]
                    queue = [(i, j)]

                    while len(queue):
                        current_cell = queue[0]
                        queue = queue[1:]

                        for neighbor in self.find_neighbors(current_cell, grid):
                            if neighbor not in visited and grid[neighbor[0]][neighbor[1]] != 0:
                                queue.append(neighbor)
                                visited.add(neighbor)
                                current_count += grid[neighbor[0]][neighbor[1]]

                    max_count = max(max_count, current_count)
        return max_count


    def find_neighbors(self, current_cell: tuple[int, int], grid: list[list[int]]) -> list[tuple[int, int]]:
        neighbors = []
        if 0 < current_cell[0]:
            neighbors.append((current_cell[0]-1, current_cell[1]))
        if 0 < current_cell[1]:
            neighbors.append((current_cell[0], current_cell[1]-1))
        if current_cell[0] < len(grid)-1:
            neighbors.append((current_cell[0]+1, current_cell[1]))
        if current_cell[1] < len(grid[0])-1:
            neighbors.append((current_cell[0], current_cell[1]+1))

        return neighbors