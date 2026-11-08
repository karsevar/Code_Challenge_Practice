class Solution:
    # The time complexity for this problem can be regarded as 0(n * m) where I'm looping through the cells in the 
    # input connected matrix one time when populating the undirected graph and a second time when traversing the 
    # resulting undirected graph using depth first search.
    # Space complexity can be calculated at 0(n*m) since the graph it self will have the same number of cells as the 
    # input connected matrix.
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # so the best way to conceptualize this problem is to view the arrays as this:
        # [ 1 first city: [first city connection, second city connection, third city connection], ...]

        # first create a graph using the information in isConnection array and then use depth first search traversal to figure out the number of provinces in the graph. The graph is indirected which means that we will need to keep track of all visited nodes or else we will hit an infinite loop.

        graph = {}

        for i in range(len(isConnected)):
            graph[i] = []
            for j in range(len(isConnected[0])):
                if i != j:
                    if isConnected[i][j] == 1:
                        graph[i].append(j)

        visited = set()
        provinces = 0
        for parent_node in graph.keys():
            if parent_node not in visited:
                queue = [parent_node]
                visited.add(parent_node)

                while len(queue):
                    current_node = queue.pop()
                    for node in graph[current_node]:
                        if node not in visited:
                            queue.append(node)
                            visited.add(node)

                provinces += 1

        return provinces