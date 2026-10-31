/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
	stack := []*Node{node}
	newNodes := map[int]*Node{}
	visited := map[*Node]bool{node: true}

	if node == nil {
		return nil
	}

	for len(stack) > 0 {
		currentNode := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		newNodes[currentNode.Val] = &Node{Val: currentNode.Val}

		for _, neighbor := range currentNode.Neighbors {
			if _, exists := visited[neighbor]; exists == false {
				stack = append(stack, neighbor)
				visited[neighbor] = true
			}
		}
	}

	stack = []*Node{node}
	visited = map[*Node]bool{node: true}

	for len(stack) > 0 {
		currentNode := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if copyNode, exists := newNodes[currentNode.Val]; exists {
			for _, neighbor := range currentNode.Neighbors {
				if copyNeighbor, exists := newNodes[neighbor.Val]; exists {
					copyNode.Neighbors = append(copyNode.Neighbors, copyNeighbor)
				}

				if _, exists := visited[neighbor]; exists == false {
					stack = append(stack, neighbor)
					visited[neighbor] = true
				}
			}
		}
	}

	return newNodes[node.Val]
}