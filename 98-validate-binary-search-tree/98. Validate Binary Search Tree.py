# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs with checking the min and max num 
        # time:O(N) space:O(N)
        def checkValid(now, minN, maxN):
            if now == None:
                return True
            # print(now.val, minN, maxN)
            if now.val<=minN or now.val>=maxN:
                return False
            # check left tree
            if not checkValid(now.left, minN, min(maxN, now.val)):
                return False
            # check right
            if not checkValid(now.right, max(minN, now.val), maxN):
                return False
            return True
        return checkValid(root, -inf, inf)