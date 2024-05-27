class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

def find(subsets, i):
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)
    return subsets[i].parent

def union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1

def spanningTree(V, adj):
    edges = []
    for i in range(V):
        for dest, weight in adj[i]:
            if i < dest:  # To avoid adding two directions of the same edge
                edges.append((i, dest, weight))
    
    edges.sort(key=lambda x: x[2])
    
    subsets = [Subset(i, 0) for i in range(V)]
    
    sumWeight = 0
    edgeCount = 0
    for edge in edges:
        src, dest, weight = edge
        src_parent = find(subsets, src)
        dest_parent = find(subsets, dest)

        if src_parent != dest_parent:
            sumWeight += weight
            union(subsets, src_parent, dest_parent)
            edgeCount += 1
            if edgeCount == V - 1:
                break
    
    return sumWeight

# Hard-coded example
V = 8  # Number of vertices
edges_list = [
    [1,2,11],
    [1,3,15],
    [1,4,9],
    [2,3,8],
    [3,4,7],
    [3,5,14],
    [3,7,17],
    [3,6,10],
    [4,5,5],
    [4,8,16],
    [5,7,4],
    [6,7,6],
    [7,8,12]
]  # Example input: edges with weights

# Convert the edge list to adjacency list
adj = [[] for _ in range(V)]
for u, v, w in edges_list:
    adj[u-1].append((v, w))
    adj[v-1].append((u, w))
print(adj)

print(spanningTree(V, adj))
