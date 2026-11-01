/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}

	clones := map[*Node]*Node{
		head: {Val: head.Val},
	}
	currentNode := head

	for currentNode != nil {
		clonedNode := clones[currentNode]
		nextNode := currentNode.Next
		randomNode := currentNode.Random

		if nextNode != nil {
			nextCloned, exists := clones[nextNode]
			if exists == false {
				nextCloned = &Node{Val: nextNode.Val}
				clones[nextNode] = nextCloned
			}
			clonedNode.Next = nextCloned
		} else {
			clonedNode.Next = nil
		}

		if randomNode != nil {
			randomCloned, exists := clones[randomNode]
			if exists == false {
				randomCloned = &Node{Val: randomNode.Val}
				clones[randomNode] = randomCloned
			}
			clonedNode.Random = randomCloned
		} else {
			clonedNode.Random = nil
		}

		currentNode = currentNode.Next
	}

	return clones[head]
}