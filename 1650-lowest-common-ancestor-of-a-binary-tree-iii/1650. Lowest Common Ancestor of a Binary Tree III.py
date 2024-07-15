"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # both p and q going to the root
        # the first node seeing p and q is the LCA
        # time: O(p to root len + q to root len)
        # space: same as time
        pParent = set()
        cur = p
        while cur!=None:
            pParent.add(cur)
            cur = cur.parent
        cur = q
        while cur!=None:
            if cur in pParent:
                return cur
            cur = cur.parent
        return None
        