from collections import deque
import copy


class Solution:
    # Basic breadth first search implementation using while loop and a queue.
    # Time complexity can be interpreted as m * n for the initial nested loop and m * n in the worst case 
    # for the traversal loop. Roughly the time complexity is O(n * m)
    # Space complexity is m * n since in the worst case we can effectively add all the cells to the visited 
    # set O(n * m)
    # This implementation only passes 40 of the 50 test cases. The main issue with this implementation is that 
    # larger paths are still being explored even when the optimal path has been found.
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # okay so we will need to find the path that is shortest between a cell that has a 1 to a cell that has a 0. We can either use breadth first search or depth first search to solve this problem and within reach traversal loop we will need to keep track of the number of 1 cells that are found for each path and calculate the path with the lowest number. 

        # we can either use a recurion function or a simple while loop with a queue. 
        # important to keep in mind that if the path hits a cell that is out of bounds we will need to return a large number that will remove that path from consideration (if using a recursion function).

        # create a nested for loop that will go through all the rows and columns of the input mat matrix.
        # we will effectively be changing the 1 values in place using the lowest path value from every traversal loop.

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    queue = [(i, j, 0)]
                    visited = set()
                    visited.add((i, j))

                    min_path = float("inf")

                    while len(queue):
                        current_i, current_j, current_count = queue[0]
                        queue = queue[1:]

                        # This additional conditional allowed me to pass up to test case 49. Through 
                        # this we can ignore all paths that already exceed the min_path count value.
                        if current_count > min_path:
                            continue

                        if mat[current_i][current_j] == 0:
                            min_path = min(min_path, current_count)
                        else:
                            for neighbor in self.find_neighbors(current_i, current_j, mat):
                                if neighbor not in visited:
                                    visited.add(neighbor)
                                    queue.append((neighbor[0], neighbor[1], current_count+1))
                    mat[i][j] = min_path
        return mat


    def find_neighbors(self, i: int, j: int, mat: list[list[int]]) -> list[tuple[int, int]]:
        neighbors = []

        if i > 0:
            neighbors.append((i-1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if i < len(mat)-1:
            neighbors.append((i+1, j))
        if j < len(mat[0])-1:
            neighbors.append((i, j+1))

        return neighbors


class SolutionEditorial:
    # editorial solution which uses the zero cells in place of the 1 cells. It turns out that my past solution 
    # was actually O(nm*2) for time complexity while this solution is O(nm). This is regarded as a multi source
    # breadth first search implementation.
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])

        queue = deque()
        distances = [[-1] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    distances[i][j] = 0

        while queue:
            current_i, current_j = queue.popleft()

            for neighbor_i, neighbor_j in self.find_neighbors(
                current_i, current_j, mat
            ):
                if distances[neighbor_i][neighbor_j] == -1:
                    distances[neighbor_i][neighbor_j] = (
                        distances[current_i][current_j] + 1
                    )
                    queue.append((neighbor_i, neighbor_j))

        return distances


    def find_neighbors(self, i: int, j: int, mat: list[list[int]]) -> list[tuple[int, int]]:
        neighbors = []

        if i > 0:
            neighbors.append((i-1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if i < len(mat)-1:
            neighbors.append((i+1, j))
        if j < len(mat[0])-1:
            neighbors.append((i, j+1))

        return neighbors