# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:21:21 2023

@author: Michael
"""

import collections

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(visited, graph, neighbour)
                
print ("DFS: ")
dfs(visited, graph, '5')