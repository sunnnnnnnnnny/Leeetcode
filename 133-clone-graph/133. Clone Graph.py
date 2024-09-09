"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # use bfs as the cloning method, where we don't go through same node twice
    # time:O(N) space:O(N)
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        newNodes = {}
        visited = set()
        bfs = []
        def cloneNode(ori):
            if ori == None:
                return None
            newN = Node(val = ori.val, neighbors = ori.neighbors)
            return newN
        
        new = cloneNode(node)
        newNodes[node] = new
        bfs.append(new)
        while bfs:
            nowLevel = len(bfs)
            for i in range(nowLevel):
                now = bfs.pop(0)
                if now in visited:
                    continue
                # print(now, new)
                newNeighbor = []
                for n in now.neighbors:
                    if n not in newNodes.keys():
                        newNeibhbor = cloneNode(n)
                        newNodes[n] = newNeibhbor
                        bfs.append(newNeibhbor)
                    newNeighbor.append(newNodes[n])
                now.neighbors = newNeighbor
                visited.add(now)
        
        return newNodes[node]

