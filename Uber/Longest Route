# import requests
# import mysql.connector
# import pandas as pd

# Given a list of itenaries, find the longest route possible among the list

# Chennai -> Hyderabad
# Hyderabad -> Bangalore
# Banaglore -> Delhi
# Hyderabad -> Delhi
# Indore -> Hyderabad

# Path1 : C -> H -> D (3 cities)
# Path2 : C -> H -> B -> D (4 cities)

from collections import defaultdict

class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        self.edges = edges
        self.graph_nodes = set()
        self.longest_route = defaultdict(list)
        self.build_graph()
        self.city_visited = set()
        
    
    def build_graph(self):
        for source, destination in self.edges:
            if not source or not destination:
                print(f"{source}->{destination} is not a valid route")
                continue
                
            self.graph[source].append(destination)
            self.graph_nodes.add(source)
            self.graph_nodes.add(destination)
    
    def dfs(self, node, path):
        self.city_visited.add(node)
        
        if len(self.graph[node]) == 0:
            self.longest_route[node] = [node]
            return [node]
        
        if node in self.longest_route:
            return self.longest_route[node]
        
        max_path = []
        for child in self.graph[node]:
            path = self.dfs(child, path + [node])
            max_path = max(max_path, path, key=len)
            # self.longest_route[child] = max(path, self.longest_route[child], key=len)
        
        self.longest_route[node] = max(self.longest_route[node], [node]+max_path)
        # print(node, self.longest_route[node])
        return self.longest_route[node]
    
    def find_longest_route(self):
        if not self.edges: return "No edge"
        
        longest_route_path = []
        
        for node in self.graph_nodes:
            if node not in self.city_visited:
                path = self.dfs(node, [])
                longest_route_path = max(longest_route_path, path, key=len)
                # print(node, path, longest_route_path)
        
        return longest_route_path


if __name__ == "__main__":
    # edges = [
    #     ("Chennai", "Hyderabad"),
    #     ("Hyderabad", "Bangalore"),
    #     ("Bangalore", "Delhi"),
    #     ("Hyderabad", "Delhi"),
    #     ("Indore", "Hyderabad"),
    # ]
    # edges = []
    
    edges = [
        ("Chennai", "")
    ]
    
    graph = Graph(edges)
    longest_route = graph.find_longest_route()
    print("Longest Route", longest_route)
