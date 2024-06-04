class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def dfs(self, start, end, path, visited, total_weight, all_paths):
        visited.add(start)
        path.append(start)

        if start == end:
            all_paths.append((path.copy(), total_weight))
        else:
            for neighbor, weight in self.graph.get(start, []):
                if neighbor not in visited:
                    self.dfs(neighbor, end, path, visited, total_weight + weight, all_paths)
        
        path.pop()
        visited.remove(start)
    
    def find_shortest_path(self, start, end):
        all_paths = []
        self.dfs(start, end, [], set(), 0, all_paths)
        
        if not all_paths:
            return None, float('inf')
        
        shortest_path, min_weight = min(all_paths, key=lambda x: x[1])
        return shortest_path, min_weight


# Contoh penggunaan:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start = 'A'
end = 'D'
shortest_path, weight = graph.find_shortest_path(start, end)

print(f"Jalur terpendek dari {start} ke {end} adalah {shortest_path} dengan bobot {weight}")
