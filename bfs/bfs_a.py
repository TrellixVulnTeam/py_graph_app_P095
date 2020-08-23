from helpers import Queue, tTack

####### BFS steps
# create queue(FIFO)
# enqueue a path to starting vertex (USE LIST)
# Create set to store visited vertices

# while queue NOT empty
#   dequeue PATH of vertices intop path variable
#   get vertex at end of path
#
#   Check if vertex NOT in visited set
#       mark as visited
#       check if vertex destination vertex
#           return path
#       
#       loop through all neighbors    
#           make copy of current path
#           add current neighbor to path copy
#           enqueue path to all neighbor vertices
#                   

def bfs(self, starting_vertex, destination_vertex):
    # create queue
    q = Queue()
    # enqueu path to starting Vertex use LIST
    q.enqueu([starting_vertex])
    # create visisted set
    visited = set()

    # while queue not empty
    if q.size() > 0:
        # dequeue Path of vertices into path variable
        path = q.dequeue()
        # get vertex at end of path
        current_vertex = path[-1]
