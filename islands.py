"""

Write a function that takes a 2D binary array and returns the number of 1 islands. 

An island consists of 1s that are connected to the north, south, east or west. 

For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]
           
island_counter(islands) # returns 4

"""

### 
# 1) Translate problem into graph terminology
## Vertices are locations where there is a 1
## edge is where 1 'touches' another 1  going north, south, east, west    

# 2) Build your graph
# 3) Traverse your graph

from util import Stack

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]



def island_counter(matrix):
    # create visited matrix
    visited = []
    for i in range(len(matrix)):   # len(matrix) is height
        visited.append([False] * len(matrix))
        # print(f' visited {visited}')

    # initialize island_count
    island_count = 0

    # loop through matrix
    #   if 1 located that is NOT visited
    #       append location to visited
    #       increment visited count
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # if node not visited
            if not visited[row][col]:
                # if 1 located at [row][col]
                if matrix[row][col] == 1:
                    # mark visited
                    # traverse all connected nodes, marking as visited
                    visited = dft(row, col, matrix, visited)

                island_count += 1

    return island_count

    
    #       traverse connected nodes, marking as visited

def dft(row, col, matrix, visited):
    # do dfs traversal


island_counter(islands)    