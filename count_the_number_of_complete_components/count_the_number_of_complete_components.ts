function countCompleteComponents(n: number, edges: number[][]): number {
    // The naive solution to this problem is to simply convert the edges array into a graph and iterate through all the nodes using depth first search to see how many of the nodes are connected.

    // first create a hash map that will contain all the connected nodes from the edges array. This will be used to count the number of completely connected components. 

    // initialize visited set that will keep track of all visited nodes
    // initialize a solutions array that will keep track of all the traversed networks

    // create a for loop that will start with 0 and end at n - 1
        // check if current node index is not in visited set if it is just simply keep node and move onto the next one.
        // initialize the stack with current node index
        // initialize a traveralMap array that will keep track of all nodes traversed
        // use depth first search to go through the generated hashmap and populate the traversalMap array with all passed nodes.

    // return length of traversal map

    let nodeMap: Map<number, Array<number>> = createNodeMap(edges)

    let visited: Set<number> = new Set()
    let solutions: Array<Array<number>> = []
    let connectedCount: number = 0

    for (let i = 0; i < n; i++) {
        if (!visited.has(i)) {
            const stack: Array<number> = [i]
            const traversalMap: Array<number> = []

            while (stack.length) {
                let currentNode: number = stack.pop()
                if (!visited.has(currentNode)) {
                    visited.add(currentNode)
                    traversalMap.push(currentNode)

                    let neighbors: Array<number> = nodeMap.get(currentNode) || []
                    
                    for (const neighbor of neighbors) {
                        if (!visited.has(neighbor)) {
                            stack.push(neighbor)
                        }
                    }
                }
            }
            
            if (traversalMap.length > 1) {
                let connected: boolean = true
                for (const solutionNode of traversalMap) {
                    let connectedNodes: number[] = nodeMap.get(solutionNode) || []
                    if (connectedNodes.length < traversalMap.length - 1) {
                        connected = false
                    }
                }
                if (connected) {
                    connectedCount += 1
                }
            } else {
                connectedCount += 1
            }
        }
    }

    return connectedCount
};

const createNodeMap = (edges: Array<Array<number>>): Map<number, Array<number>> => {
    const graph: Map<number, Array<number>> = new Map();

    for (let [a, b] of edges) {
        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);
        graph.get(a).push(b);
        graph.get(b).push(a);
    }

    return graph
}