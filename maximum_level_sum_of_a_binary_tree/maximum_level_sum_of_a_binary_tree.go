type QueueValue struct {
	Node  *TreeNode
	Level int
}

func maxLevelSum(root *TreeNode) int {
	queue := []QueueValue{}
	levelValues := map[int]int{}

	if root == nil {
		return 0
	}

	queue = append(queue, QueueValue{Node: root, Level: 1})

	for len(queue) > 0 {
		currentValue := queue[0]
		queue = queue[1:]

		if _, exists := levelValues[currentValue.Level]; exists {
			levelValues[currentValue.Level] += currentValue.Node.Val
		} else {
			levelValues[currentValue.Level] = currentValue.Node.Val
		}

		if currentValue.Node.Left != nil {
			queue = append(queue, QueueValue{Node: currentValue.Node.Left, Level: currentValue.Level + 1})
		}

		if currentValue.Node.Right != nil {
			queue = append(queue, QueueValue{Node: currentValue.Node.Right, Level: currentValue.Level + 1})
		}
	}

	highestLevel := [2]int{1, levelValues[1]}

	for level, count := range levelValues {
		if highestLevel[1] < count {
			highestLevel = [2]int{level, count}
		}
	}

	return highestLevel[0]
}