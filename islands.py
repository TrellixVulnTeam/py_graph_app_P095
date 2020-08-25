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
## find the location (coordinates) for each 1 
# 3) Traverse your graph
## since we are traversing graph, bft OR dft BOTH gives us all vertices
## get_neighbors to the RESCUE, find 

from util import Stack, Queue

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# # returns 4


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0]]
# returns 4


# islands = [[0, 0, 0, 0, 0],
#            [0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0]]
# returns 4

# islands = [[0, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0]]
# returns 3



# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
# 13

def island_counter(matrix):
    # create visited matrix
    visited = []
    island = {}

    for i in range(len(matrix)):   # len(matrix) is height
        visited.append([False] * len(matrix[0]))
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
                    # print(f'\t current [row][col] [{row}][{col}]   ')
                    # traverse all connected nodes, marking as visited
                    # visited = dft(row, col, matrix, visited)
                    visited = bft(row, col, matrix, visited)
                    # increment count
                    island_count += 1


    # print(f' island {island}')
    # for item in island:
    #     print(f' item {item} ')
    
    return island_count

    
    #       traverse connected nodes, marking as visited

def dft(start_row, start_col, matrix, visited):
    # create Stack
    s = Stack()
    # push starting vertex
    s.push((start_row, start_col))    # use a tuple cause they are immutable & can be used as dict key
 
    while s.size() > 0:
        # pop first vertex
        v = s.pop()
        row = v[0]
        col = v[1]

        # check if already visited
        if not visited[row][col]:
            visited[row][col] = True
            # push all neighbors onto stack
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
                print(f'n >>  {neighbor}')
    return visited

def bft(start_row, start_col, matrix, visited):
    # create Stack
    q = Queue()
    # enqueue starting vertex
    q.enqueue((start_row, start_col))    # use a tuple cause they are immutable & can be used as dict key
    island_connected = []
    island_c = {}
    path_d = set()
    path_d.add((start_row, start_col))
    


    while q.size() > 0:
        # dequeue first vertex
        v = q.dequeue()
        row = v[0]# 
        col = v[1]

        # check if already visited
        if not visited[row][col]:
            visited[row][col] = True


            # push all neighbors onto queue
            for neighbor in get_neighbors(row, col, matrix):                
                q.enqueue(neighbor)
                # print(f'n >>  {neighbor}')  
             
                #  
                if neighbor not in island_connected:
                    island_connected.append(neighbor)    
                    # path_d[(start_row, start_col)] = neighbor
                    path_d.add(neighbor)
            if (row, col) not in island_connected:
                island_connected.append((row, col))

                  
    print(f'    connected:   {path_d}')
    # print(f' \n island_connections  {island_connected} ')                
    return visited


def get_neighbors(row, col, matrix):
    # return list of neighboring 1 tuples in form [(row, col)]
    neighbors = []

    #  check north
    if row > 0 and matrix[row -1][col] == 1:
        neighbors.append( (row-1, col) )
    # check south
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append( (row + 1, col)  )
    # check east
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append( (row, col + 1)  ) 
    # check west           
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append( (row, col - 1) )
    
    return neighbors          


print(island_counter(islands))    