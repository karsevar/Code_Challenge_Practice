class Solution:
    # First attempt only passing 32 of the 54 test cases. Will need to refactor this solution a little more
    # to pass all test cases. Perhaps the correct intuition is to use a topological sort to determine if there is a cycle in the graph. If there is a cycle, then it is impossible to finish all courses. If there is no cycle, then it is possible to finish all courses.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # so the best way to think about this problem is to see the input prerequisites array as a kind of graph where the first index of edge 0 is the required class and the second index of edge 0 is the prerequisite. 

        # so first the best idea is to transform the input array into a graph where it looks like this {a^0: b^0, a^1: b^1} and so on.

        if len(prerequisites) <= 0:
                return True

        class_graph = {}
        for edge in prerequisites:
            if edge[0] in class_graph:
                class_graph[edge[0]].add(edge[1])
            else:
                class_graph[edge[0]] = set()
                class_graph[edge[0]].add(edge[1])

        print(class_graph)

        return self.recursion_helper(
            prerequisites[0][0],
            class_graph,
            numCourses
        )

    def recursion_helper(
        self, 
        edge: int,
        class_graph: dict[int,set[int]],
        numCourses: int
    ) -> bool:
        if numCourses == 1:
            if edge not in class_graph:
                return True

        elif numCourses > 0:
            if edge in class_graph:
                for neighbor in class_graph[edge]:
                    if self.recursion_helper(
                        neighbor,
                        class_graph,
                        numCourses-1
                    ):
                        return True
                    

        return False


class SolutionRevisiteWithDFS:
    # Passes 48 out of 55 test cases since I'm disounting paths that end in the same terminal not as other 
    # concurrent paths. As a means to get around this issue is to employ the two visited set method where one 
    # set keeps track of the current course path (and can be used to detect if a cycle is present) and another 
    # set that keeps track of all the nodes that were already visited. 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        course_map = {} # course map will look like {course bi: [ai]}

        for classes in prerequisites:
            class_a, class_b = classes
            print("class_a: ", class_a, " class_b: ", class_b)
            if class_b not in course_map:
                course_map[class_b] = [class_a]
            else:
                course_map[class_b].append(class_a)
        
        for classNum in range(len(prerequisites)):
            if classNum in course_map:
                stack = [classNum]
                visited = set()
                visited.add(classNum)

                while len(stack):
                    current_class = stack.pop()

                    for neighbor in course_map[current_class]:
                        if neighbor not in visited and neighbor in course_map:
                            visited.add(neighbor)
                            stack.append(neighbor)
                        elif neighbor in visited and neighbor in course_map:
                            return False
                break
            
        return True



        

    

        