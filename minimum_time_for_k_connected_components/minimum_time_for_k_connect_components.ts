// initial attempt. It only passes 2 of the initial 3 test cases since this solution does not account for already disconnected nodes which have time zero.
const minTime = (n: number, edges: number[][], k: number): number => {

    // I believe the best course of action is to separate out the values of edges array into a graph like data structure meaning that it will be a hashmap that contains {"node_u": [["node_v", "time"]]}
    // keep in mind that the conceptual graph is undirected meaning that the depth first search algorithm can go in both directions hence a seen set datastructure will be needed to keep track of the visited nodes thus decreasing the possibility of infinite loops.

    // Main questions to keep in mind when designing the code:
    // - What constituates time? In the second example it says that 4 is the answer since the last connected nodes time is 4. This part kind of feels ambiguous since we disconnected edges 0 and 2 and the time is 2 for that disconnection. 
    // - K value seems straightforward since we are actively keeping track of the number of nodes we are disconnecting. This will be the number of nodes in which the algorithm will stop.
    // - I believe that the start node is the first value in the provided array. In the case of example 2 that start is node 0. Will the start node always be 0 for all the test cases?

    // initial try: first create a hashtable with the provided node values in the edges array. And use the resulting hash map to use a depth first search algorithm implementation. stopping condition will be when the number of processed nodes equals k. node count will be kept during the duration of the depth first search algorithm.

    // initialize node_map hash map

    // create a for loop that will loop through edges
        // for each edges entry create key value pairs.
        // logic
        // if edges[i][0] key not in node_map add edges[i][0] as key and edges[i][1] and edges[i][2] as values.
        // if edges[i][1] key not in node_map add edges[i][1] as key and edges[i][0] and edges[i][2] as values.
        // else just simply add edges[i][1] or edges[i][0] as values in their corresponding keys.

    // the resulting hashmap should look like this node_map = {"node": [["node", "time"], ....]}

    // initialize depth first search algorithm
    // initialize an empty stack variable
    // initialize visited set variable
    // initialize node count by one
    // add the first node in the edges array example [0, 2]

    // create a while loop that will terminate once stack is empty.
    // get current node from stack
    // check if current element has been visited
    // if not add node to visited array 
    // iterate node count by one
    // check if node count is equal to k 
    // if so return the current node's time value current_node[1]
    // if not get neighbors arrays from the node_map node_map[current_node[0]]
    // if neighbor node is not in visited set add them to the stack.

    // return 0 if the minimum time can not be found.

    const nodeMap: Map<number, number[][]> = new Map();

    for (let i = 0; i < edges.length; i++) {
        if (!nodeMap.has(edges[i][0])) {
            nodeMap.set(edges[i][0], [[edges[i][1], edges[i][2]]])
        } else {
            let nodeArray = nodeMap.get(edges[i][0])
            nodeArray.push([edges[i][1], edges[i][2]])
        }

        if (!nodeMap.has(edges[i][1])) {
            nodeMap.set(edges[i][1], [[edges[i][0], edges[i][2]]])
        } else {
            let nodeArray = nodeMap.get(edges[i][1])
            nodeArray.push([edges[i][0], edges[i][2]])
        }
    }

    console.log("nodeMap: ", nodeMap)

    const stack: Array<Array<number>> = new Array()
    stack.push([edges[0][0], edges[0][2]])
    let nodeCount: number = 0
    const visited: Set<number> = new Set()

    while (stack.length > 0) {
        let currentNode: Array<number> = stack.pop()
        if (!visited.has(currentNode[0])) {
            visited.add(currentNode[0])
            nodeCount += 1

            if (nodeCount === k) {
                return currentNode[1]
            }

            const neighbors: Array<Array<number>> = nodeMap.get(currentNode[0])
            for (let i = 0; i < neighbors.length; i++) {
                if (!visited.has(neighbors[i][0])) {
                    stack.push(neighbors[i])
                }
            }
        }
    }

    return 0
}