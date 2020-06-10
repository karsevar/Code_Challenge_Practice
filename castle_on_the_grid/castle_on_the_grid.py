def minimumMoves(grid, startX, startY, goalX, goalY):
    # print(grid)
    # print('start', startX, startY)
    # print('goal', goalX, goalY)

    # create a get neighbors function that will be able to check 
    # if the nodes to the right, left, top, and bottom of the current 
    # node exists or is an x.

    def get_neighbors(indexX, indexY, grid):
        # neighbors array will take in the coordinates as (x, y)
        neighbors = []
        # if X value to the right of indexX is not the end of the passed in string 
        # or is not x 
            # add the node x and y coordinates to the neighbors array

        # if x value to the left of indexX is not less than the index 0 or 
        # is not x 
            # add the node x and y coordinates to the neighbors array 

        # if y value on top of indexY is not equal to -1 or x 
            # add the node x and y corrdinates to the neighbors array

        # if y value on the bottom of indexY is not more than the Y axis of the 
        # grid or equal to x 
            # add the node x and y coordinates to the neighbors array

        if (indexX + 1) < len(grid[0]): 
            if grid[indexX+1][indexY] != 'X':
                neighbors.append((indexX+1, indexY, 'R'))

        if (indexX - 1) >= 0:
            if grid[indexX-1][indexY] != 'X':
                neighbors.append((indexX-1, indexY, 'L'))

        if (indexY-1) >= 0:
            if grid[indexX][indexY-1] != 'X':
                neighbors.append((indexX, indexY-1, 'U'))

        if (indexY + 1) < len(grid):
            if grid[indexX][indexY+1] != 'X':
                neighbors.append((indexX, indexY+1, 'D'))
    
        return neighbors
    
    print(get_neighbors(startX, startY, grid))

    # create the breadth first traversal algorithm:
    # first create a queue 
    # create a visited set 

    # initialize the queue with the starting node coordinates in 
    # (x, y, direction) format, Make sure to structure the queue elements 
    # as an array inside an array example [[(x, y, direction), ...]] to keep 
    # track of traversal path 

    # create a while loop that will terminate once the queue is empty 
    #   pop the direction from the beginning of the queue 
    #   check if the last item in the popped path is not in visited 
    #       if so add the node to the visited set 
    #       add the neighbors to the queue 

    queue = []
    queue.append([(startX, startY, 'S')])
    result_path = []

    visited = set() 

    while len(queue) > 0:
        path = queue.pop(0)

        if path[-1] not in visited:

            if path[-1][0] == goalX and path[-1][1] == goalY:
                result_path = list(path)
                break

            for neighbor in get_neighbors(path[-1][0], path[-1][1], grid):
                new_path = list(path)
                new_path.append(neighbor) 
                queue.append(new_path)

    moves = 0
    past_move = 'S'

    for direction in result_path:
        if past_move != direction[2]:
            moves += 1
            past_move = direction[2]

    return moves