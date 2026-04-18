// This is my initial attempt. It is only passing 25 out of 36 test cases.
function makeConnected(n: number, connections: number[][]): number {
    // it seems that the none connected computers are not apart of the original function input so part of the things that we are attempting to solve is the number of unconnected computers (unconnected nodes within the connections array) as well as the number of redundent connects (connections that for a cycle).
    // two places that we will need to keep count of the number of unconnected computers and the number of connections that form a cycle between computers.

    // create a graph map that will organize the nodes into the following data structure:
    // computerMap = {"computer_node": ["computer_node1", "computer_node2"]}

    // create a visited set that will keep track of the node that we already evaluated.

    // initialize a unconnected computer counter set it 0

    // create a for loop that will start from 0 to n - 1

    // initialize an empty stack

    // add current node to stack

    // dfs algorithm 

    // while loop that will terminate once stack is empty

    // check if node is in visited.
    // if not add node to visited set and get neighbors from computerMap 
    // if computer is not in computerMap then iterate unconnected computer counter by one
    // if computer has neighbors iterate through neighbors array by checking if they are in visited if they are not in visited than add them to the stack
        // perhaps this might be where I can add additional logic that will keep track of the number of cycles.

    // check if unconnected computers is less than or equal to number of cycles if not true then return -1 if true return the number of unconnected computers

    // time complexity
    // O(C) Creating the computerMap since we have to go through the connections array
    // O(V) We need to traverse the contents of computerMap which means that we will visit each distinct vertex 
    // time complexity O(C + V)

    if (n - 1 > connections.length) {
        return -1
    }

    const computerMap: Map<number, Array<number>> = new Map()

    for (let [a, b] of connections) {
        if (!computerMap.has(a)) computerMap.set(a, []);
        if (!computerMap.has(b)) computerMap.set(b, []);
        computerMap.get(a).push(b);
        computerMap.get(b).push(a);
    }

    let unconnectedComputers: number = 0 
    let cycleCount: number = 0

    const visited: Set<number> = new Set()

    for (let i = 0; i < n; i++) {
        if (!computerMap.has(i)) {
            unconnectedComputers += 1
        } else {
            let cycles: number = dfs(computerMap, visited, i)
            cycleCount += cycles
        }
    }

    console.log("unconnectedComputers:", unconnectedComputers)
    console.log("cycles: ", cycleCount)

    if (Math.floor(cycleCount) >= unconnectedComputers) {
        return unconnectedComputers
    }
    return -1

};

function dfs(computerMap: Map<number, Array<number>>, visited: Set<number>, computer: number): number {
    const stack: Array<number> = [computer]

    const traversalRoute: Array<number> = []

    let cycles: number = 0
    
    while (stack.length) {
        let currentComputer: number = stack.pop()
        if (!visited.has(currentComputer)) {
            visited.add(currentComputer)
            traversalRoute.push(currentComputer)

            let neighbors: Array<number> = computerMap.get(currentComputer) || []

            for (const neighbor of neighbors){
                if (!visited.has(neighbor)) {
                    stack.push(neighbor)
                } else {
                    cycles += 0.5
                }
            }
        }
    }

    return cycles
}