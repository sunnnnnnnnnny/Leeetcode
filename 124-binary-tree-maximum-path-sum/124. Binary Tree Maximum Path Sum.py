# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs getting the left&right sum and return the max path child
        maxPathSum = -inf
        def dfsSum(now):
            nonlocal maxPathSum
            if now == None:
                return 0
            leftPathSum = dfsSum(now.left)
            rightPathSum = dfsSum(now.right)
            overNowPath = leftPathSum+now.val+rightPathSum
            maxPathSum = max(maxPathSum, overNowPath)
            includeNowPath = max(leftPathSum, rightPathSum)+now.val
            includeNowPath = max(includeNowPath, now.val)
            maxPathSum = max(maxPathSum, includeNowPath)
            return includeNowPath
        dfsSum(root)
        return maxPathSum