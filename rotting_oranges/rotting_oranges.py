class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # the main question that I have is whether there is only one rotten orange or are there multiple rotten oranges in the matrix. Will make a basic solution that assumes that there is only one rotten orange. 

        # will compose an initial outer loop that goes through the rows and columns of the matrix until we run into a rotten orange that we haven't yet explored. 
        # min_minutes = 0
        # orange_traversal_counts = []
        # total_oranges = 0

        # okay so the actual way that you should answer this question is through breadth first search and populating the queue with multiple starting points before initializing the traversal.
        # time complexity is O(m*n) for going through each column and row of the grid just to find all the rotten oranges and in the worst case the traversal algorithm will be O(m*n) since we will be going through each cell again.
        # the space complexity is O(n*m) in the worst case since both the queue and visited set can grow to the same size as the input grid.

        queue = []
        visited = set()
        total_oranges = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 2:
                    queue.append((0, j, i))
                    visited.add((j, i))
                    total_oranges += 1
                if grid[j][i] == 1:
                    total_oranges += 1

        orange_traversal_count = ()
        total_minutes = 0

        while len(queue):
            current_minutes, current_row, current_column = queue[0]
            queue = queue[1:]
            total_minutes = max(total_minutes, current_minutes)

            for neighbor in self.find_neighbors(current_row, current_column, grid):
                if neighbor not in visited:
                    if grid[neighbor[0]][neighbor[1]] == 1:
                        queue.append((current_minutes+1, neighbor[0], neighbor[1]))
                        visited.add((neighbor[0], neighbor[1]))
        orange_traversal_count = (total_minutes, len(visited))

        return orange_traversal_count[0] if orange_traversal_count[1] == total_oranges else -1

    
    def find_neighbors(self, j: int, i: int, board: list[list[int]]) -> list[tuple[int, int]]:
        neighbors = []

        if j < len(board)-1:
            neighbors.append((j+1, i))
        if i < len(board[0])-1:
            neighbors.append((j, i+1))
        if j > 0:
            neighbors.append((j-1, i))
        if i > 0:
            neighbors.append((j, i-1))
        return neighbors