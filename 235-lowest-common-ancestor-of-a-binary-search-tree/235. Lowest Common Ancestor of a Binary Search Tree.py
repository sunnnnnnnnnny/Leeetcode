# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # according to the characteristic of BST
        # if a number x is p<=x<=q then it shall be the LCA
        # by DFS accessing to x, if now>q go left, if now<q go right
        # time: O(N) space:O(N)
        pval = min(p.val, q.val)
        qval = max(p.val, q.val)
        def findLCA(now: 'TreeNode'):
            nonlocal pval, qval
            if now == None:
                return None
            if now.val>=pval and now.val<=q.val:
                return now
            if now.val>qval:
                return findLCA(now.left)
            if now.val<pval:
                return findLCA(now.right)
            return now
        return findLCA(root)
        