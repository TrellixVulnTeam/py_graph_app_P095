def total_edges(n, directed = False):
    result =  (n*(n-1) // 2)

    if directed:
        return result * 2

    return result


for i in range(10):
    print(f' num vertices {i} \t directed max total edges: {total_edges(i)} \t undirected max total edges {total_edges(i, True)}')    

#  num vertices 0          directed max total edges: 0     undirected max total edges 0
#  num vertices 1          directed max total edges: 0     undirected max total edges 0
#  num vertices 2          directed max total edges: 1     undirected max total edges 2
#  num vertices 3          directed max total edges: 3     undirected max total edges 6
#  num vertices 4          directed max total edges: 6     undirected max total edges 12
#  num vertices 5          directed max total edges: 10    undirected max total edges 20
#  num vertices 6          directed max total edges: 15    undirected max total edges 30
#  num vertices 7          directed max total edges: 21    undirected max total edges 42
#  num vertices 8          directed max total edges: 28    undirected max total edges 56
#  num vertices 9          directed max total edges: 36    undirected max total edges 72
# 
#   