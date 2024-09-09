# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # postorder is left->right->root
        # with dfs, time;O(N) spce:O(N)
        ret = []
        def dfsPost(now):
            nonlocal ret
            if now == None:
                return
            dfsPost(now.left)
            dfsPost(now.right)
            ret.append(now.val)
        dfsPost(root)
        return ret
