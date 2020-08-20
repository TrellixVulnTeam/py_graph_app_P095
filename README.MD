# Graph problems 

### 3 steps to solve graph problems

1) Translate problem into graph terminology
2) Build your graph
3) Traverse your graph


###  Sparse vs. Dense graphs
- So, the maximum total number of edges possible is |E| = |V|x|V| = |V|^ 2
- A graph that is “close to” having |V|^2 edges is considered dense
- A graph that is “closer to” having |V| edges is considered sparse


### Total Number of Edges possible
- Total number of edges in a complete graph of N vertices = ( n * ( n – 1 ) ) / 2

~~~ py
def total_edges(n):
    return  (n*(n-1) // 2)

~~~