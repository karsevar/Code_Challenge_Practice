class Solution:
    # this isn't really the best solution as I'm defining two different traversal logic components for grid1 and grid2
    # All the test cases pass but understandably this is not the most efficient method as I'm traversing through each 
    # grid in their own separated loop and I can perhaps consolidate everything into it's own nested for loop where 
    # I traverse grid1 first and use the output island locations to while I loop through grid2.
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        visited_grid1 = set()

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1 and (i, j) not in visited_grid1:
                    self.recursion_helper((i, j), visited_grid1, grid1)

        island_count = 0

        visited_grid2 = set()
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited_grid2:
                    queue = [(i, j)]
                    visited_grid2.add((i, j))

                    count_island = False
                    if (i, j) in visited_grid1:
                        count_island = True

                    while len(queue):
                        current_index = queue.pop()

                        for neighbor in self.find_neighbors(current_index, grid2):
                            if grid2[neighbor[0]][neighbor[1]] == 1 and neighbor not in visited_grid2:
                                visited_grid2.add(neighbor)
                                queue.append(neighbor)
                                if neighbor not in visited_grid1:
                                    count_island = False

                    if count_island:
                        island_count += 1

        return island_count


    def find_neighbors(self, current_index: tuple[int, int], grid: list[list[int]]) -> list[tuple[int, int]]:
        neighbors = []

        if current_index[0] > 0:
            neighbors.append((current_index[0]-1, current_index[1]))
        if current_index[1] > 0:
            neighbors.append((current_index[0], current_index[1]-1))
        if current_index[0] < len(grid)-1:
            neighbors.append((current_index[0]+1, current_index[1]))
        if current_index[1] < len(grid[0])-1:
            neighbors.append((current_index[0], current_index[1]+1))

        return neighbors

                    


    def recursion_helper(self, current_index: tuple[int, int], visited: set[tuple[int, int]], grid: list[list[int]]):
        if current_index[0] < 0 or current_index[1] < 0 or current_index[0] >= len(grid) or current_index[1] >= len(grid[0]):
            return 

        if grid[current_index[0]][current_index[1]] == 0 or current_index in visited:
            return

        visited.add(current_index)
        self.recursion_helper((current_index[0]-1, current_index[1]), visited, grid)
        self.recursion_helper((current_index[0]+1, current_index[1]), visited, grid)
        self.recursion_helper((current_index[0], current_index[1]-1), visited, grid)
        self.recursion_helper((current_index[0], current_index[1]+1), visited, grid)