class Solution:
    # Bruteforce solution using breadth first search and a visited set as a means to keep the algorithm from running into infinite loop. In efficiencies can be seen with my converting lists into tuples since we need to keep track of all the visited bombs within a set. In addition we have a breadth first search traversal loop wrapped in a for loop which means that we are looping through the bombs array O(n^2). Perhaps we are looping through the bombs array a little more since the find_nearby_bombs function loops through the bombs array as well.
    # only passes 177 of the 199 test cases.
    def find_nearby_bombs(self, current_bomb: list[int], bombs: list[list[int]]) -> list[list[int]]:
        nearby_bombs = []
        for index, bomb in enumerate(bombs):
            # Circle Equation used (x - h)^2 + (y - k)^2 <= r^2
            # where bomb is conceptualized as (x, y) and current bomb is conceptualized as (h, k)
            if pow((bomb[0] - current_bomb[0]), 2) + pow((bomb[1] - current_bomb[1]), 2) <= pow(current_bomb[2], 2):
                nearby_bombs.append([*bomb, index])

        return nearby_bombs



    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        # okay it seems that we can use either depth first search or breadth first search for this problem. We can have a outer loop that sits above the depth first search loop that supplies the starting bomb positions since this problem does not provide an actual starting position bomb.
        # for each iteration of the depth first search loop we will need to find out if
        ## 1.) if the current bomb's blast radius is within the range of other bombs in the array. And if so we will need to add them to the queue.
        ## 2.) each iteration of the breadth first search loop will need to translate to one increment of the bomb number counter.

        max_bombs = 0

        for index, bomb in enumerate(bombs):
            copied_bomb = [*bomb, index]
            queue = [copied_bomb]
            bomb_counter = 0
            visited = set()
            visited.add(tuple(copied_bomb))

            while len(queue):
                current_bomb = queue[0]
                queue = queue[1:]
                bomb_counter += 1

                # we will need to get all the bombs that fall within the blast radius of the current bomb and that haven't been visited yet.
                for nearby_bomb in self.find_nearby_bombs(current_bomb, bombs):
                    if tuple(nearby_bomb) not in visited:
                        queue.append(nearby_bomb)
                        visited.add(tuple(nearby_bomb))

            max_bombs = max(max_bombs, bomb_counter)

        return max_bombs


class SolutionEditorial:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        # editorial solution: Was able to cut down a lot of the time complexity through separating the neighboring bomb look up to outside the breadth first search traversal loop. This is achieved through simply creating the traversal graph before initializing the traversal loop.

        graph = {}

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    x1, y1, r1 = bombs[i]
                    x2, y2, r2 = bombs[j]
                    dist = pow((x1 - x2), 2) + pow((y1 - y2), 2) 
                    if dist <= pow(r1, 2):
                        if i not in graph:
                            graph[i] = [j]
                        else:
                            graph[i].append(j)

        queue = []
        maxCount = float('-inf')

        for node in range(len(bombs)):
            if node in graph:
                queue.append(node)
                visited = set()
                visited.add(node)
                count = 0

                while len(queue):
                    current_node = queue[0]
                    queue = queue[1:]
                    count += 1
                    maxCount = max(maxCount, count)
                    if current_node in graph:
                        for child in graph[current_node]:
                            if child not in visited:
                                visited.add(child)
                                queue.append(child)

        return maxCount if maxCount != float('-inf') else 1