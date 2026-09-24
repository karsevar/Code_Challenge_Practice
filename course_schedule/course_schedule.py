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