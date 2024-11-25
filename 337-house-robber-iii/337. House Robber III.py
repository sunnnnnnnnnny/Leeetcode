# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # choosing the child or parent
        # dfs with postOrder traversal, to collect the numbers includ child and not
        # time:O(N) space:O(N)
        house = []
        def postOrder(now):
            nonlocal house
            if now == None:
                return 0, 0
            maxPreLeft, maxLeft = postOrder(now.left)
            maxPreRight, maxRight = postOrder(now.right)
            maxChild = maxLeft+maxRight
            maxWithSelf = now.val+maxPreLeft+maxPreRight
            return maxChild, max(maxWithSelf, maxChild)
        maxnoRoot, maxRoot = postOrder(root)
        return max(maxnoRoot, maxRoot)
