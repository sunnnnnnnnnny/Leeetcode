# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # postorder is left child, right child, parent
        # by backtracking we can get the order
        # time:O(N) the size of the tree
        # space: O(N) dp recursive
        ret = []
        def postOrder(now):
            if now is None:
                return []
            leftChild = postOrder(now.left)
            rightChild = postOrder(now.right)
            leftChild.extend(rightChild)
            leftChild.append(now.val)
            return leftChild
        return postOrder(root)


        