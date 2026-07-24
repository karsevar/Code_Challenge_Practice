# brutefore method only passes 43 out of 65 test cases. Will need to think about a possible cache for words that are similar to 
# one another to decrease time complexity.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # this looks almost like the word search 1 problem I just finished.

        # the main difference is I will need to either create an externial loop that will check for the first letter of each word in the words array and begin looping through the board using the recursion function.

        # other than the addition of the words array I believe that we can use the same method as last time given that time complexity will be really high.

        # create a for loop that will loop through each individual word in the words array. 
            # within the outer loop we will need to create a visited set that will carry the visited indexes (i,j)
            # create word_queue that will be initialized using the current word
            # create a for loop over the columns j index
            # create a for loop over the rows i index
                # if the first letter of the current word is found in board[j][i] 
                # add the current (i, j) index to visited
                # call recursive function using state, word_queue, visited, and results as arguments
                # if results is not empty add word to outer results list

        words_found = []
        for word in words:
            word_found = False
            word_queue = list(word)
            for j in range(len(board)):
                for i in range(len(board[j])):
                    if word_queue[0] == board[j][i]:
                        visited = set()
                        visited.add((i, j))
                        results = []
                        self.recursion_helper([word_queue[0]], i, j, word_queue[1:], board, results, visited)
                        # print("results: ", results)
                        if len(results) > 0:
                            words_found.append(word)
                            word_found = True
                            break
                if word_found:
                    break

        return words_found


    def recursion_helper(self, state: List[str], i: int, j: int, word_queue: List[str], board: List[List[str]], results: List[str], visited):
        # base case will be if word_queue is empty add state to results array

        # recursive if word_queue is not empty
        # create for loop that will get the neighbors of the current index position in the board
        # check if neighbor is not in visited set
            # if true 
            # add neighbor to state
            # call recursive function with updated neighbor indexes, word_queue, state
            # remove neighbor from state
            # remove neighbor from visited set

        # print("state: ", state, " word_queue: ", word_queue, " results: ", results)

        if len(word_queue) == 0:
            # print("word found join: ", "".join(state[:]))
            results.append("".join(state[:]))
            # print("results: ", results)
            return
        
        elif len(word_queue) > 0:
            for neighbor in self.get_neighbors(i, j, board):
                if neighbor not in visited:
                    if board[neighbor[1]][neighbor[0]] == word_queue[0]:
                        state.append(word_queue[0])
                        visited.add(neighbor)
                        self.recursion_helper(state, neighbor[0], neighbor[1], word_queue[1:], board, results, visited)
                        state.pop()
                        visited.remove(neighbor)
                        

    def get_neighbors(self, i: int, j: int, board: List[List[str]]) -> List[tuple[int, int]]:
        neighbors = []
        if j+1 < len(board):
            neighbors.append((i, j+1))
        if j-1 >= 0:
            neighbors.append((i, j-1))
        if i + 1 < len(board[j]):
            neighbors.append((i+1, j))
        if i - 1 >= 0:
            neighbors.append((i-1, j)) 

        return neighbors