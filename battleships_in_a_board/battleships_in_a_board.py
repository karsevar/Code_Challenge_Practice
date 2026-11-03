class Solution:
    # time complexity can be conceptualized as O(N * M ) where we are going through each cell within the input matrix
    # for the inner DFS loop we are visiting each "x" cell once given that we are saving all visited coordinates in 
    # a set.
    # space complexity is O(n*M) in the worst case.
    def countBattleships(self, board: list[list[str]]) -> int:
        # this problem can be thought of as a normal depth first search problem where the entry point can be one of the many coordinates in the matrix. So we will need to have an outer nested for loop that will go through and assess every [i][j] coordinate in the matrix. We will need to keep track of all the visited coordinates as a means to keep the algorithm from double counting X coordinates.

        ship_count = 0
        visited = set()

        for j in range(len(board)):
            for i in range(len(board[0])):
                if board[j][i] == "X" and (j, i) not in visited:
                    visited.add((j, i))
                    self.recursion_helper(
                        (j, i),
                        board,
                        visited,
                    )
                    ship_count += 1
                    # call recursion function that will take in the following arguments
                    # visited, currentIndex ([j, i])
                    # make sure to increment ship_count by one

        return ship_count

    def recursion_helper(self, currentIndex: tuple[int, int], board: list[list[str]], visited: set[tuple]):
        for neighbor in self.find_neighbors(currentIndex, board):
            if board[neighbor[0]][neighbor[1]] == "X" and neighbor not in visited:
                visited.add(neighbor)
                self.recursion_helper(neighbor, board, visited)

    def find_neighbors(self, currentIndex: tuple[int, int], board: list[list[str]]) -> list[tuple[int, int]]:
        neighbors = []

        if currentIndex[0] < len(board)-1:
            neighbors.append((currentIndex[0]+1, currentIndex[1]))
        if currentIndex[1] < len(board[0])-1:
            neighbors.append((currentIndex[0], currentIndex[1]+1))
        if currentIndex[0] > 0:
            neighbors.append((currentIndex[0]-1, currentIndex[1]))
        if currentIndex[1] > 0:
            neighbors.append((currentIndex[0], currentIndex[1]-1))
        return neighbors