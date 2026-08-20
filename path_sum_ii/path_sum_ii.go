package pathsumii

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// The time complexity for this solution is more in line with O(n) since unlike the python solution I'm
// not copying the state of the path for every recursive call.
func pathSum(root *TreeNode, targetSum int) [][]int {
	// first create an array that will carry the resulting paths of the depth first search traversal.

	// create a recursive function that will be used to loop through the entire tree structure and add the node to leaf paths that add up to the target sum.

	// return results

	results := [][]int{}

	recursiveHelper(
		[]int{},
		root,
		targetSum,
		&results,
	)

	return results
}

// recursiveHelper function will take in state, treeNode, targetSum, and results. and will not return anything since it will be writing to a pointer of results
func recursiveHelper(state []int, treeNode *TreeNode, targetSum int, results *[][]int) {
	if treeNode != nil && treeNode.Left == nil && treeNode.Right == nil {
		if (targetSum - treeNode.Val) == 0 {
			dupState := append([]int{}, state...)
			dupState = append(dupState, treeNode.Val)
			*results = append(*results, dupState)
		}
		return
	}

	if treeNode != nil {
		state = append(state, treeNode.Val)
		if treeNode.Left != nil {
			recursiveHelper(
				state,
				treeNode.Left,
				targetSum-treeNode.Val,
				results,
			)
		}

		if treeNode.Right != nil {
			recursiveHelper(
				state,
				treeNode.Right,
				targetSum-treeNode.Val,
				results,
			)
		}
	}
}
