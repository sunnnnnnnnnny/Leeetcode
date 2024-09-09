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
        bfs = []
        def cloneNode(ori):
            if ori == None:
                return None
            newN = Node(val = ori.val)
            return newN
        bfs.append(node)
        new = cloneNode(node)
        newNodes[node] = new
        while bfs:
            nowLevel = len(bfs)
            for i in range(nowLevel):
                now = bfs.pop(0)
                modify = newNodes[now]
                # print(now, new)
                for n in now.neighbors:
                    if n not in newNodes.keys():
                        bfs.append(n)
                        NewNeibhbor = cloneNode(n)
                        newNodes[n] = NewNeibhbor
                    modify.neighbors.append(newNodes[n])
        
        return newNodes[node]

