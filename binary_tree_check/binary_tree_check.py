def check_binary_search_tree_(root):
    
    # First create an inorder traversal function that will 
    # save all the node values in ascending order in an array 
    # arguments are the root node and the node array 
        # check if the passed in root node is not None 
            # if yes recursively call the util function on the left and right nodes 
            # in the middle of the two recursive calls append the current_node's value 
            # into the node array 
    
    node_array = []
    def inorder_traversal(current_node, node_array):
        if current_node != None:
            inorder_traversal(current_node.left, node_array)
            node_array.append(current_node.data)
            inorder_traversal(current_node.right, node_array)
            
    inorder_traversal(root, node_array)
    
    for index in range(len(node_array)-1):
        if node_array[index] >= node_array[index + 1]:
            return False
        
    return True