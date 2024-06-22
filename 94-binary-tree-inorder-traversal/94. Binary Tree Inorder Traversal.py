# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(cur):
            if cur == None:
                return []
            left = dfs(cur.left)
            right = dfs(cur.right)
            return left+[cur.val]+right
        return dfs(root)
        