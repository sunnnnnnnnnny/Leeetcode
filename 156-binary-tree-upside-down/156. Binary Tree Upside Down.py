# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # it's like in-order traversal b/c we get left first then root, right
        # time:O(N) space:O(N)
        newRoot = None
        def inOrder(now):
            nonlocal newRoot
            if now.left == None:
                if newRoot == None:
                    newRoot = now
                return
            
            newLeftRoot = now.left
            inOrder(now.left)
            newLeftRoot.left = now.right
            newLeftRoot.right = now
            now.left = None
            now.right = None
            return
        if root == None:
            return None
        inOrder(root)
        return newRoot