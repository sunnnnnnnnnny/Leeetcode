# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # using dfs to get the both target
        # time:O(N) space:O(N)
        ret = None
        def dfs(now, pFound, qFound):
            nonlocal q, p, ret
            if now == None:
                return False, False
            if pFound and qFound:
                return pFound, qFound
            leftp, leftq = dfs(now.left, pFound, qFound)
            rightp, rightq = dfs(now.right, pFound, qFound)
            pFound = leftp or rightp
            qFound = leftq or rightq

            if not pFound and now == p:
                pFound = True
            if not qFound and now == q:
                qFound = True

            if pFound and qFound and ret == None:
                ret = now
            return pFound, qFound
        dfs(root, False, False)
        return ret