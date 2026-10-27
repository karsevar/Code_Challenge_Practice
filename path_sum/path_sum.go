/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, targetSum int) bool {
	return recursionHelper(root, targetSum, 0)
}

func recursionHelper(root *TreeNode, targetSum int, currentSum int) bool {
	result := false
	if root != nil {
		if root.Left == nil && root.Right == nil {
			if currentSum+root.Val == targetSum {
				return true
			}
		}

		if root.Left != nil || root.Right != nil {
			if recursionHelper(root.Left, targetSum, currentSum+root.Val) {
				result = true
			}

			if recursionHelper(root.Right, targetSum, currentSum+root.Val) {
				result = true
			}
		}
	}

	return result
}