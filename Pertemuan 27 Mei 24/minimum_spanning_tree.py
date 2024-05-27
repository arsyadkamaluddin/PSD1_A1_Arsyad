import heapq
class Graph():
    def __init__(self):
        self.graph = {}
        self.node_map = {}
        self.reverse_node_map = []

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    def set_vertices(self,V):
        self.V = V
    def set_nodes(self, nodes):
        self.node_map = {node: index for index, node in enumerate(nodes)}
        self.reverse_node_map = nodes

    def prim_mst(self):
        start_node = self.reverse_node_map[0]
        start_index = self.node_map[start_node]
        
        visited = [False] * self.V
        distance = [float('inf')] * self.V
        parent = [None] * self.V
        
        distance[start_index] = 0
        min_heap = [(0, start_index)]
        
        while min_heap:
            dist, u = heapq.heappop(min_heap)
            visited[u] = True
            
            for v, w in self.graph[self.reverse_node_map[u]]:
                v_index = self.node_map[v]
                if not visited[v_index] and w < distance[v_index]:
                    distance[v_index] = w
                    parent[v_index] = u
                    heapq.heappush(min_heap, (w, v_index))
        
        result = []
        print("Minimum Spanning Tree menggunakan Prim-Dijkstra:")
        tot_distance = 0
        for i in range(1, self.V):
            if parent[i] is not None:
                u = self.reverse_node_map[parent[i]]
                v = self.reverse_node_map[i]
                w = distance[i]
                tot_distance += w
                print(f"{u}->{v} == {w}")
                result.append([parent[i], i, w])
        print(f"Total = {tot_distance}")
        return result

edges = [
    ('A', 'B', 11), ('A', 'D', 9), ('A', 'C', 15), ('D', 'E', 5), ('D', 'C', 7),
    ('D', 'G', 16), ('B', 'C', 8), ('C', 'F', 10), ('C', 'E', 14), ('C', 'H', 17),
    ('E', 'H', 4), ('H', 'F', 6), ('G', 'H', 12), ('B', 'A', 11), ('D', 'A', 9),
    ('C', 'A', 15), ('C', 'D', 7), ('E', 'D', 5), ('C', 'B', 8), ('F', 'C', 10),
    ('E', 'C', 14), ('H', 'C', 17), ('H', 'E', 4), ('F', 'H', 6), ('H', 'G', 12),
    ('G', 'D', 16)
]
g = Graph()
g.set_vertices(len(edges))
nodes = []

for u,v,w in edges :
    if u not in nodes:nodes.append(u)
    if v not in nodes:nodes.append(v)
    g.add_edge(u, v, w)

g.set_nodes(nodes)


prim_result = g.prim_mst()