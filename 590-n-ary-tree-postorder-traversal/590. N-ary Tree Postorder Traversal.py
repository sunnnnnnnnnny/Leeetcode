"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # time:O(N) size of the tree 
        # space:O(N)
        ret = []
        def postNary(now):
            nonlocal ret
            if now == None:
                return
            # print(len(now.children))
            for ch in now.children:
                postNary(ch)
            ret.append(now.val)
        postNary(root)
        return ret
        