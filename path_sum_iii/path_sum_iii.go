func pathSum(root *TreeNode, targetSum int) int {
	return recursionHelper(
		root,
		[]int{},
		targetSum,
	)
}

func recursionHelper(root *TreeNode, currentPath []int, targetSum int) int {
	if root == nil {
		return 0
	}

	currentPath = append(currentPath, root.Val)

	pathCount := 0
	currentSum := 0

	for i := len(currentPath) - 1; i >= 0; i-- {
		currentSum += currentPath[i]
		if currentSum == targetSum {
			pathCount += 1
		}
	}

	pathCount += recursionHelper(
		root.Left,
		currentPath,
		targetSum,
	)

	pathCount += recursionHelper(
		root.Right,
		currentPath,
		targetSum,
	)

	currentPath = currentPath[:len(currentPath)-1]
	return pathCount
}