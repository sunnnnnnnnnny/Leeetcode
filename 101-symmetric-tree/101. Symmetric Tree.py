# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # the child val should be mirrow of itself, with dfs comparing the nodes
        # time:O(N) space:O(N)
        # bfs to record it's the left or right tree to check
        def compLeftRight(l, r):
            if l == None and r==None:
                return True
            elif l == None or r==None:
                return False
            if l.val == r.val:
                if compLeftRight(l.left, r.right) and compLeftRight(l.right, r.left):
                    return True
            return False
        if root == None:
            return True
        return compLeftRight(root.left, root.right)