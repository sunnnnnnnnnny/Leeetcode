# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # common ancestor would be min(p,q)<=a<=max(p,q)
        # recursive to get the a by crateria
        # does it gurantee the p and q in the tree? assume yes
        # time:O(N) treesize, space:O(N)
        if p == None or q == None:
            return None
        aSmall = min(p.val, q.val)
        aBig = max(p.val, q.val)
        def findA(now, small, big):
            if now == None:
                return None
            if now.val>=small and now.val<=big:
                return now
            if now.val<small:
                # on the right side
                return findA(now.right, small, big)
            return findA(now.left, small, big)
        return findA(root, aSmall, aBig)