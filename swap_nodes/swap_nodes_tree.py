#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #

    def swap_nodes(indexes, query):
        # create a queue since I'm going to use level order traversal 
        # each entry in the queue will be in the format (level, index value)

        # create a loop that will terminate once the queue is empty 
            # pop the head off of the queue 

            # if the popped value is not -1 
                # if the popped value's level is a multiple of query 
                    # swap the right and left nodes 

                # enqueue the left and right nodes through the data structure 
                # (indexes[index[1]-1][0], index[0] + 1) for the left and right nodes
                # (node value, node level)

        queue = []
        # initialize the queue with the first root value in the node tree
        queue.append((1, 1))

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node[0] != -1:
                if current_node[1] %query == 0:
                    new_right = indexes[current_node[0] - 1][0]
                    new_left = indexes[current_node[0] - 1][1]

                    indexes[current_node[0] - 1] = [new_left, new_right]

                # enqueue the new left and right nodes
                queue.append((indexes[current_node[0] - 1][0], current_node[1] + 1))
                queue.append((indexes[current_node[0] - 1][1], current_node[1] + 1))

    def inorder_traversal(indexes, solution_string):
        # if index == -1:
        #     return
        # if index != -1:
        #     # subtract 1 from the input index because the 
        #     # array is zero indexed
        #     inorder_traversal(indexes, indexes[index-1][0], solution_string)
        #     solution_string.append(index)
        #     inorder_traversal(indexes, indexes[index-1][1], solution_string)

        stack = []
        current_node = 1
        # stack.append(index)

        while True:
            if current_node != -1:
                stack.append(current_node)
                current_node = indexes[current_node - 1][0]
            elif len(stack) > 0:
                current_node = stack.pop()
                solution_string.append(current_node)
                current_node = indexes[current_node - 1][1]
            else:
                break

        return solution_string 

    # create a for loop that will iterate through all the queries in the queries array
    results = [] 
    for query in queries:
        solution_string = []
        swap_nodes(indexes, query)
        solution_string = inorder_traversal(indexes, solution_string)
        # string_convert = ''
        # for value in solution_string:
        #     string_convert += str(value)
        results.append(solution_string)

    return results

    # new_string = inorder_traversal(indexes, 1, solution_string)
    # print(new_string)