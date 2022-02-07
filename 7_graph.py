# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:04:09 2022

@author: Akshatha
"""

class Graph():
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = self.convert_to_dict()
      
    def convert_to_dict(self):
        node_dict = {}
        for orig,dest in self.edges:
            if orig in node_dict.keys():
                node_dict[orig].append(dest)
            else:
                node_dict[orig] = [dest]   
        return node_dict
    
    def find_paths(self, origin, destination):
        paths = []
        if origin in self.graph_dict.keys():
            for node in self.graph_dict[origin]:
                if node==destination:
                    paths.append([origin,node])
                else:
                    for path in self.find_paths(node, destination):
                        paths.append([origin]+path)
        return paths
    
    def find_shortest_path(self, origin, destination, path =[]):
        path = path + [origin]
        
        if origin ==destination:
            return path
        
        if origin not in self.graph_dict.keys():
            return None
        
        shortest_path = None
        for node in self.graph_dict[origin]:
            if node not in path:
                sp = self.find_shortest_path(node, destination, path)
                if sp:
                    if shortest_path is None or len(sp) <= len(shortest_path):
                        shortest_path = sp
        return shortest_path
                            
         
    def find_shortest_paths(self, origin, destination):
        # brute force
        paths = self.find_paths(origin, destination)
        lengths = [len(path) for path in paths]
        min_paths = [path for path in paths if len(path) == min(lengths)]
        return min_paths
    
if __name__ == '__main__':
    routes = [
        ('Mumbai','Paris'),
        ('Mumbai','Dubai'),
        ('Dubai','New York'),
        ('Paris','Dubai'),
        ('Paris','New York'),
        ('New York','Toronto'),
        ('Dubai','Toronto')
        ]
    route_graph = Graph(routes)
    print(route_graph.convert_to_dict())
    print(route_graph.find_paths('Mumbai', 'New York'))
    print(route_graph.find_shortest_path('Mumbai', 'New York'))