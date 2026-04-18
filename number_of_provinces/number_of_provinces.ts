function findCircleNum(isConnected: number[][]): number {
    // Okay since the given data structure is a n * n matrix we can conceptualize the hashmap as 
    // {"city 1": [city 1, city 2], ...} we can effectively create the hashmap through first iterating through isConnected i index to get the city key value and the neighboring city connections. It's important to keep in mind that each city will mostlikely be connected with itself hence creating an undirected graph. Which means that visited set will be needed to avoid infinite loops. 

    // dfs will be used to traverse all connected cities starting with city 1. Each pass through the dfs algorithm will populate the visited set. A province is a combination of connected or unconnected cities which means that a network of connected cities only for one province.

    // initialize empty cityMap hashtable variable 
    // create a for loop that will iterate through isConnected.lenth i index
    // Add i as a new key in cityMap with an empty array as a value
    // create a nested for loop that will iterate through i index neighbors j index
    // push all the j index values to the value array if they are 1

    // initialize a visited set
    // initialize provincesCount variable

    // create for loop that will start at 0 and end at isConnected.length - 1
    // if conditional that checks if i city was visited 
    // if not call dfs helper function and iterate provincesCount by one

    // return provincesCount

    // time complexity seems to be a combination of the dimensions of the n * n matrix in isConnected.
    // This means that the initial nested for loop that composes the cityMap is O(n * m) or rather O(n^2)
    // While the traversal algorithm might have a time complexity of o(n) since it is going through each city vertex once 
    // combined O(n^2 + n)

    // Space complexity is o(n^2 + n) since we are populating cityMap with all the contents of isConnected n * n matrix and we are populating the visited set with a total of n possible cities.

    const cityMap: Map<number, Array<number>> = new Map();

    for (let i = 0; i < isConnected.length; i++) {
        cityMap.set(i, [])
        for (let j = 0; j < isConnected[i].length; j++) {
            if (isConnected[i][j] === 1) {
                cityMap.get(i).push(j)
            }
        }
    }

    console.log("cityMap: ", cityMap)

    const visited: Set<number> = new Set();
    let provinces: number = 0

    for (let city = 0; city < isConnected.length; city++) {
        if (!visited.has(city)) {
            dfs(cityMap, visited, city)
            provinces += 1
        }
    }
    return provinces
};


function dfs(cityMap: Map<number, Array<number>>, visited: Set<number>, city: number) {
    const stack: Array<number> = [city]
    console.log("visited: ", visited)
    while (stack.length) {
        let currentCity: number = stack.pop()
        if (!visited.has(currentCity)) {
            visited.add(currentCity)

            let neighbors: Array<number> = cityMap.get(currentCity) || []
            for (let neighbor of neighbors) {
                if (!visited.has(neighbor)) {
                    stack.push(neighbor)
                }
            }
        }
    }
}