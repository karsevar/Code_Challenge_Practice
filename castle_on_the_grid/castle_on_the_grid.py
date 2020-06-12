#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque 

# Complete the minimumMoves function below.
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

        x_axis = indexX + 1
        while x_axis < len(grid[0]):
            if grid[x_axis][indexY] != 'X':
                neighbors.append((x_axis, indexY))
                x_axis += 1
            else:
                break

        x_axis = indexX - 1
        while x_axis >= 0:
            if grid[x_axis][indexY] != 'X':
               neighbors.append((x_axis, indexY))
               x_axis -= 1 
            else:
                break

        y_axis = indexY - 1
        while y_axis >= 0:
            if grid[indexX][y_axis] != 'X':
                neighbors.append((indexX, y_axis))
                y_axis -= 1
            else:
                break
        
        y_axis = indexY + 1
        # print('indexY', indexY)
        
        while y_axis < len(grid):
            # print('y_axis after up movement 2', grid[indexX][y_axis])
            if grid[indexX][y_axis] != 'X':
                neighbors.append((indexX, y_axis))
                y_axis += 1
            else:
                break 

        # find the coordinate with the highest or lowest X value 
        highest_xcoordinate = neighbors[0]
        lowest_xcoordinate = neighbors[0]
        highest_ycoordinate = neighbors[0]
        lowest_ycoordinate = neighbors[0]
        
        for x_coordinate in neighbors[1:]:
            if x_coordinate[0] > highest_xcoordinate[0]:
                highest_xcoordinate = x_coordinate 
            if x_coordinate[0] < lowest_xcoordinate[0]:
                lowest_xcoordinate = x_coordinate

            if x_coordinate[1] > highest_ycoordinate[1]:
                highest_ycoordinate = x_coordinate 

            if x_coordinate[1] < lowest_ycoordinate[1]:
                lowest_ycoordinate = x_coordinate 
        
        # print('neighbors full array', neighbors)

        # print('neighbors print', lowest_ycoordinate, highest_ycoordinate, lowest_xcoordinate, highest_xcoordinate)

        # return [highest_xcoordinate, lowest_xcoordinate, highest_ycoordinate, lowest_ycoordinate]

        return neighbors
    
    # print(get_neighbors(startX, startY, grid))

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
    queue.append([(startX, startY)])
    result_path = []

    visited = set() 

    while len(queue) > 0:
        path = queue.pop(0)
        print(path)

        if path[-1] not in visited:
            visited.add(path[-1])

            if path[-1][0] == goalX and path[-1][1] == goalY:
                result_path= path
                

            for neighbor in get_neighbors(path[-1][0], path[-1][1], grid):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor) 
                    queue.append(new_path)

    print(result_path)

    return len(result_path) - 1