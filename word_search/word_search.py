class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # okay so for this problem it will be best to think of this as a depth first search problem. 

        # the first course of action is to find all the adjacent cells that are attached to each letter in the matrix. We can begin through compiling the graph of each individual letter cell to make the depth first search algorithm easier to reason about or we can compile them within the recursive function using the matrix position i (for horizontal) and j (for vertical).
        # can't compile the graph first since there are repeat values in the matrix and usually graphs are compiled in map form.

        # to limit the search space we can convert the word variable into an array and use it as some make shift stack where in the choice stage of the backtrack algorithm we check if a choice is a valid letter. This can cut down possible paths that the algorithm will check. 

        # create backtrack_helper recursive function that will have board, i index, j index, state, and word_array as arguments. 

        word_array = list(word)
        results = []
        # visited = set() # I think I can add indexes in tuple form (i, j)

        for j in range(len(board)):
            for i in range(len(board[j])):
                # print("visited: ", visited)
                if board[j][i] == word_array[0]:
                    visited = set()
                    visited.add((i, j))
                    self.backtrack_helper([board[j][i]], i, j, word_array[1:], board, results, visited)

        return len(results) > 0

    def backtrack_helper(self, state: List[str], i: int, j: int, word_array: List[str], board: List[List[str]], results: List[List[str]], visited):
        # base case will be if word array is an empty array then that means that the current state array has all the required letter and can be included in the results array.

        # recursive state:
        # create a for loop that will loop through the neighbors of the current matrix index position through the use of another helper function.
        # check if the first letter in word_array is equal to a specific neighbor
        # if a neighbor fits add neighbor to the state array
        # call the recurive function 

        # print("results: ", results)
        # print("word_array: ", word_array)
        # print("state: ", state)
        if len(word_array) <= 0:
            results.append(state[:])
        else:
            for neighbor in self.find_neighbors(i, j, board):
                if board[neighbor[1]][neighbor[0]] == word_array[0] and neighbor not in visited:
                    state.append(board[neighbor[1]][neighbor[0]])
                    visited.add(neighbor)
                    self.backtrack_helper(
                        state,
                        neighbor[0],
                        neighbor[1],
                        word_array[1:],
                        board,
                        results,
                        visited
                    )
                    state.pop()
                    visited.remove(neighbor)

    def find_neighbors(self, i: int, j: int, board: List[List[int]]):
        neighbors = [] # will contain tuple with i and j indexes
        if i + 1 < len(board[j]):
            neighbors.append((i+1, j))
        
        if j + 1 < len(board):
            neighbors.append((i, j + 1))

        if i - 1 >= 0:
            neighbors.append((i - 1, j))

        if j - 1 >= 0:
            neighbors.append((i, j- 1))

        return neighbors