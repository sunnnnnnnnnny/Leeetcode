# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs from the root, assuming not an cycle graph since it's a Tree
        # time:O(N) space:O(N)
        # maxDepth = 0
        def dfs(now, curDepth):
            if now == None:
                return curDepth
            leftDepth = dfs(now.left, curDepth+1)
            rightDepth = dfs(now.right, curDepth+1)
            return max(leftDepth, rightDepth)
        return dfs(root, 0)
