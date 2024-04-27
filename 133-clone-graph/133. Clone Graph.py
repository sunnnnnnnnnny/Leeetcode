"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # using DFS or BFS to go through the graph
    # Both time cost=O(N+M) edge and node
    # Using visited to record the relationship of ori node and new node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        self.visited = {}
        def cloneDfs(self, node):
            if not node:
                return node
            if node in self.visited:
                return self.visited[node]
        
            new_node = Node(node.val, [])
            self.visited[node] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(cloneDfs(self, neighbor))
            return new_node
        return cloneDfs(self,node)
        

        