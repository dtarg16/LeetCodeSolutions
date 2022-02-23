"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def rec(self, node):

        if node.val in self.visited:
            return self.nodes[node.val]
        
        self.visited.append(node.val)
        
        new_node = self.nodes[node.val]
        for neighbor in node.neighbors:
            new_neighbor = self.nodes[neighbor.val]
            new_node.neighbors.append(new_neighbor)
            
        for neighbor in node.neighbors:
            self.rec(neighbor)
    
    def traverse(self, node):
        if node.val not in  self.nodes:
            self.nodes[node.val] = Node(node.val, [])
            for neighbour in node.neighbors:
                self.traverse(neighbour)
                

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node
        self.nodes = {}
        self.traverse(node)
        self.visited = []
        self.rec(node)
        return self.nodes[node.val]
        
        
        
        