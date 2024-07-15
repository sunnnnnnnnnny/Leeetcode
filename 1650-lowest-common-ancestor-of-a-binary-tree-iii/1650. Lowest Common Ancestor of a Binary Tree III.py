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
        # get both len of p and q to root
        # move the lower one
        # allowing p and q start on the same height to seek LCA
        # time:O((height(p)+height(q))*2)
        # space:O(1)
        def findHeight(now):
            if now == None:
                return 0
            return findHeight(now.parent)+1
        pHeight = findHeight(p)
        qHeight = findHeight(q)
        pPar = p
        qPar = q
        if pHeight>qHeight:
            for _ in range(pHeight-qHeight):
                pPar = pPar.parent
        elif pHeight<qHeight:
            for _ in range(qHeight-pHeight):
                qPar = qPar.parent
        while pPar != qPar:
            pPar = pPar.parent
            qPar = qPar.parent
        return pPar
        # both p and q going to the root
        # the first node seeing p and q is the LCA
        # time: O(p to root len + q to root len)
        # space: same as time
        # pParent = set()
        # cur = p
        # while cur!=None:
        #     pParent.add(cur)
        #     cur = cur.parent
        # cur = q
        # while cur!=None:
        #     if cur in pParent:
        #         return cur
        #     cur = cur.parent
        # return None
        