
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if (root === null) {
        return false
    }
    // console.log("root node: ", root.val)
    // console.log("hasPathSumHelper function: ", hasPathSumHelper(root, targetSum))
    return hasPathSumHelper(root, targetSum)
};

function hasPathSumHelper(treeNode: TreeNode | null, targetSum: number): boolean {
    if (treeNode !== null) {
        // console.log("\n targetSum: ", targetSum)
        // console.log("treeNode value: ", treeNode.val)
        if (treeNode.left === null && treeNode.right === null && targetSum - treeNode.val === 0) {
            return true
        }

        return hasPathSumHelper(treeNode.left, targetSum - treeNode.val) || hasPathSumHelper(treeNode.right, targetSum - treeNode.val)
    } else {
        return false
    }
} 