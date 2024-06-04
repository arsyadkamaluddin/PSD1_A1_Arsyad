from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def bfs(self, start, end):
        # Priority queue to handle BFS with weights
        queue = [(0, start, [])]  # (total weight, current node, path)
        visited = set()
        
        while queue:
            total_weight, node, path = heapq.heappop(queue)
            
            if node in visited:
                continue
            
            path = path + [node]
            visited.add(node)
            
            if node == end:
                return path, total_weight
            
            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (total_weight + weight, neighbor, path))
        
        return None, float('inf')

# Contoh penggunaan:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start = 'A'
end = 'D'
shortest_path, weight = graph.bfs(start, end)

print(f"Jalur terpendek dari {start} ke {end} adalah {shortest_path} dengan bobot {weight}")
