class Solution:
    # Basic depth first search solution where the simplified time complexity is O(n*m) where n is the rows of 
    # the input matrix and m is the columns of the input matrix. We are actually traversing through the matrix 
    # two times in total the outer for loops are going through each cell while the inner depth first search loop
    # is going through every cell in the matrix in the worst case. Though time complexity is controlled through 
    # the use of the visited set which keeps us from reassessing already viewed 1 cells.

    # Space complexity can be O(n*m) in the worst case as well since the visited set can grow into the same size
    # as the matrix.
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # it seems that max area can be conceptualized as the number of 1 cells that a island cluster has. 
        # the most straightforward solution is to use depth first search to traverse 1 cell clusters whenever a 1 cell cluster is reach.
        # We will need an outer for loop that will iterate through all the cells in the matrix and we will call the traversal loop when a 1 cell is reached. Important to keep in mind that we should have a common visited set as a means to keep us from assessing the same island clusters.
        # max_area variable will be initialized outside of the nested for loop
        visited = set()
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    stack = [(i, j)]
                    visited.add((i, j))
                    current_area = 1
                    while len(stack):
                        current_cell = stack.pop()
                        for neighbor in self.find_neighbors(current_cell, grid):
                            if grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in visited:
                                current_area += 1
                                stack.append(neighbor)
                                visited.add(neighbor)

                    max_area = max(current_area, max_area)

        return max_area


    def find_neighbors(self, current_cell: tuple[int, int], grid: list[list[int]]) -> list[tuple[int, int]]:
        neighbors = []
        if current_cell[0] > 0:
            neighbors.append((current_cell[0]-1, current_cell[1]))
        if current_cell[1] > 0:
            neighbors.append((current_cell[0], current_cell[1]-1))
        if current_cell[0] < len(grid)-1:
            neighbors.append((current_cell[0]+1, current_cell[1]))
        if current_cell[1] < len(grid[0])-1:
            neighbors.append((current_cell[0], current_cell[1]+1))

        return neighbors