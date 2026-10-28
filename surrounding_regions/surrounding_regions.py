class Solution:
    # understandably this isn't the best solution as I'm pretty much looping through the entire matrix once during the outer loop which will be n * m by itself but than I'm also looping traversing every connected "O" cell using a depth first search traversal algorithm and in addition I'm looping through the visited set twice. Will need to consolidate all of these loops.
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # the best way to probably solve this is to use depth first search and actively change the current O cell to X if it is flanked by another O cell horizontally or vertically.

        # one thing to keep in mind is that we will need to assess whether the cell is flanked by similar cells or if it is already surrounded by X cells. This will be challenging in the depth first search loop since if we change the cells in place the last cell will not be converted.
        # fix might be to collect all the O cell coordinates during the depth first search loop and convert them over to X outside of the depth first search loop.

        # create an outer loop that will go through the each cell from row to column
        for j in range(len(board)):
            for i in range(len(board[0])):
                if board[j][i] == "O":
                    # call a recursive function that will return all coordinates of adjacent 
                    # "O" cells 

                    # [(j, i), ...]
                    visited = set()
                    visited.add((j, i))

                    self.dfs(
                        (j, i),
                        board,
                        visited,
                    )

                    switch = True
                    for cell in visited:
                        if cell[0] == 0 or cell[0] == len(board) - 1 or cell[1] == 0 or cell[1] == len(board[0])-1:
                            switch = False

                    if switch == True:
                        for cell in visited:
                            board[cell[0]][cell[1]] = "X"

    
    def dfs(self, currentCell: tuple[int, int], board: List[List[str]], results: set[tuple[int, int]]):
        # create recursion for loop that will loop through all neighbors.

        for neighbor in self.findNeighbors(currentCell, results, board):
            if board[neighbor[0]][neighbor[1]] == "O" and neighbor not in results:
                results.add(neighbor)
                self.dfs(
                    neighbor,
                    board,
                    results,
                )

    def findNeighbors(self, currentCell: tuple[int, int], results: set[tuple[int, int]], board: List[List[str]]) -> List[tuple[int, int]]:
        neighbors = []

        if currentCell[0] > 0:
            neighbors.append((currentCell[0] - 1, currentCell[1]))
        if currentCell[0] < len(board) - 1:
            neighbors.append((currentCell[0]+1, currentCell[1]))
        if currentCell[1] > 0:
            neighbors.append((currentCell[0], currentCell[1]-1))
        if currentCell[1] < len(board[0]) - 1:
            neighbors.append((currentCell[0], currentCell[1]+1))

        return neighbors

        