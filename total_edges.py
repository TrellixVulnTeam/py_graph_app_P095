def total_edges(n, directed = False):
    result =  (n*(n-1) // 2)

    if directed:
        return result * 2

    return result


for i in range(10):
    print(f' num edges {i} \t directed max total edges: {total_edges(i)} \t unidrected total edges {total_edges(i, True)}')    

#  num edges 0 total edges: 0
#  num edges 1 total edges: 0
#  num edges 2 total edges: 1
#  num edges 3 total edges: 3
#  num edges 4 total edges: 6
#  num edges 5 total edges: 10
#  num edges 6 total edges: 15
#  num edges 7 total edges: 21
#  num edges 8 total edges: 28  
# 
#   