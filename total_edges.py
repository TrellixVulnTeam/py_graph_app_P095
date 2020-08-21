def total_edges(n, directed = False):
    result =  (n*(n-1) // 2)

    if directed:
        return result * 2

    return result


for i in range(10):
    print(f' num edges {i} \t directed max total edges: {total_edges(i)} \t undirected max total edges {total_edges(i, True)}')    

#  num edges 0     directed max total edges: 0     undirected total edges 0
#  num edges 1     directed max total edges: 0     undirected total edges 0
#  num edges 2     directed max total edges: 1     undirected total edges 2
#  num edges 3     directed max total edges: 3     undirected total edges 6
#  num edges 4     directed max total edges: 6     undirected total edges 12
#  num edges 5     directed max total edges: 10    undirected total edges 20
#  num edges 6     directed max total edges: 15    undirected total edges 30
#  num edges 7     directed max total edges: 21    undirected total edges 42
#  num edges 8     directed max total edges: 28    undirected total edges 56
#  num edges 9     directed max total edges: 36    undirected total edges 72 
# 
#   