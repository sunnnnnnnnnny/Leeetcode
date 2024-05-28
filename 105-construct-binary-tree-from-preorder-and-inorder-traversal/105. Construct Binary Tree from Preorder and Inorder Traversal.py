# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # using the preorder to get the root of the tree
        # then with inorder we can spearate the tree by root into left, right
        inorder_hash_map = {}
        for idx, val in enumerate(inorder):
            inorder_hash_map[val] = idx
        
        # the preorder root idx
        preorder_idx = 0

        def inorder_build_tree(left:int, right:int):
            nonlocal preorder_idx
            if left>right:
                return None
            # get the root node
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1
            root.left = inorder_build_tree(left, inorder_hash_map[root_val]-1)
            root.right = inorder_build_tree(inorder_hash_map[root_val]+1, right)
            return root
        return inorder_build_tree(0, len(inorder)-1)