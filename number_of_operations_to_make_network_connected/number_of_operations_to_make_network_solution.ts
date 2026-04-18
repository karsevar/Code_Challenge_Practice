// Actual solution from looking at the solutions discussion on leetcode. 
function makeConnected(n: number, connections: number[][]): number {
    // time complexity
    // O(C) Creating the computerMap since we have to go through the connections array
    // O(V) We need to traverse the contents of computerMap which means that we will visit each distinct vertex 
    // time complexity O(C + V)

    // Space complexity
    // O(C) Creating the computerMap hashtable from the values in connections array.
    // O(V) from creating the visited set which will have at most V entries
    // space complexity O(C + V)

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

    const visited: Set<number> = new Set()

    for (let i = 0; i < n; i++) {
        if (!visited.has(i)) {
            dfs(computerMap, visited, i)
            unconnectedComputers += 1
        }
    }
    return unconnectedComputers - 1

};

function dfs(computerMap: Map<number, Array<number>>, visited: Set<number>, computer: number) {
    const stack: Array<number> = [computer]
    
    while (stack.length) {
        let currentComputer: number = stack.pop()
        if (!visited.has(currentComputer)) {
            visited.add(currentComputer)

            let neighbors: Array<number> = computerMap.get(currentComputer) || []

            for (const neighbor of neighbors){
                if (!visited.has(neighbor)) {
                    stack.push(neighbor)
                }
            }
        }
    }
}