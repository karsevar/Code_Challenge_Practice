func findCircleNum(isConnected [][]int) int {
	graph := map[int][]int{}

	for i := 0; i < len(isConnected); i++ {
		graph[i] = []int{}
		for j := 0; j < len(isConnected); j++ {
			if i != j && isConnected[i][j] == 1 {
				if nodes, exists := graph[i]; exists {
					graph[i] = append(nodes, j)
				}
			}
		}
	}

	visited := map[int]bool{}
	provinces := 0

	for parent_node := range graph {
		if _, exists := visited[parent_node]; exists == false {
			queue := []int{
				parent_node,
			}
			visited[parent_node] = true

			for len(queue) > 0 {
				current_node := queue[0]
				queue = queue[1:]

				for _, node := range graph[current_node] {
					if _, exists := visited[node]; exists == false {
						queue = append(queue, node)
						visited[node] = true
					}
				}
			}

			provinces += 1
		}
	}

	return provinces
}