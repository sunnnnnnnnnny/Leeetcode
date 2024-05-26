# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # switch all the child node of left and right
        # dfs or bfs traverse
        # time: O(N) space:O(N)
        def dfs(cur: Optional[TreeNode]):
            if cur == None:
                return cur
            newLeft = dfs(cur.left)
            newRight = dfs(cur.right) 
            cur.left = newRight
            cur.right = newLeft
            return cur
        newRoot = dfs(root)
        return newRoot
        