type QueueElement struct {
	TreeLevel   int
	CurrentNode *Node
}

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}

	queue := []QueueElement{
		{1, root},
	}

	results := map[int][]*Node{}

	for len(queue) > 0 {
		currentElement := queue[0]
		queue = queue[1:]

		if nodes, exists := results[currentElement.TreeLevel]; exists == false {
			results[currentElement.TreeLevel] = []*Node{currentElement.CurrentNode}
		} else {
			nodes = append(nodes, currentElement.CurrentNode)
			results[currentElement.TreeLevel] = nodes
		}

		if currentElement.CurrentNode.Left != nil {
			queue = append(queue, QueueElement{TreeLevel: currentElement.TreeLevel + 1, CurrentNode: currentElement.CurrentNode.Left})
		}

		if currentElement.CurrentNode.Right != nil {
			queue = append(queue, QueueElement{TreeLevel: currentElement.TreeLevel + 1, CurrentNode: currentElement.CurrentNode.Right})
		}
	}

	for _, nodes := range results {
		for i := 0; i < len(nodes); i++ {
			if i == len(nodes)-1 {
				nodes[i].Next = nil
			} else {
				nodes[i].Next = nodes[i+1]
			}
		}
	}

	return root
}