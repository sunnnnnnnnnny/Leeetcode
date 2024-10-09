"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # bfs traversal 
        # time: O(N) the size of the nodes
        ret = []
        if root == None:
            return ret
        nextElement = [root]
        while nextElement:
            levelCnt = len(nextElement)
            levelEle = []
            for _ in range(levelCnt):
                now = nextElement.pop(0)
                levelEle.append(now.val)
                for child in now.children:
                    nextElement.append(child)
            ret.append(levelEle)
        return ret
