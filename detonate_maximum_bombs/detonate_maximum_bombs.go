import "math"

func maximumDetonation(bombs [][]int) int {
	graph := map[int][]int{}

	for i := 0; i < len(bombs); i++ {
		for j := 0; j < len(bombs); j++ {
			if i != j {
				dist := math.Pow(float64(bombs[i][0]-bombs[j][0]), 2) + math.Pow(float64(bombs[i][1]-bombs[j][1]), 2)
				if dist <= math.Pow(float64(bombs[i][2]), 2) {
					if value, exists := graph[i]; exists {
						value = append(value, j)
						graph[i] = value
					} else {
						graph[i] = []int{
							j,
						}
					}
				}
			}
		}
	}

	queue := []int{}
	maxCount := math.Inf(-1)

	for node := 0; node < len(bombs); node++ {
		if _, exists := graph[node]; exists {
			queue = append(queue, node)
			visited := map[int]bool{}
			visited[node] = true
			count := 0

			for len(queue) > 0 {
				current_node := queue[0]
				queue = queue[1:]
				count += 1
				if float64(count) > maxCount {
					maxCount = float64(count)
				}

				if _, exists := graph[current_node]; exists {
					for _, child := range graph[current_node] {
						if _, exists := visited[child]; exists == false {
							visited[child] = true
							queue = append(queue, child)
						}
					}
				}
			}
		}
	}

	if maxCount == math.Inf(-1) {
		return 1
	}

	return int(maxCount)
}