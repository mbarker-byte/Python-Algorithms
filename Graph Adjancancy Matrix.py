# -*- coding: utf-8 -*-
"""
Created on Wed May 24 23:10:54 2023

@author: Michael
"""

class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        
        def add_edge(self, v1, v2):
            if v1 == v2:
                print ("Same vertex %d and %d" % (v1, v2))
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v2] = 1
            
        def remove_edge(self, v1, v2):
            if self.adjMatri[v1][v2] == 0:
                print("No edge betweem %d and %d" % (v1, v2))
                return
            
        def __len__(self):
            for row in self.adjMatrix:
                for val in row:
                    print('{:4}'.format(val)),
                print
                
def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    
    g.print_matrix()
    
if __name__ =='__main__':
    main()