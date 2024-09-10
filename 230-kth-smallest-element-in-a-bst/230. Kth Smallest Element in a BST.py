# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST the left is smaller
        # preorder traversal to get the Kth smallest element, 
        # by recording how many node it have discovered
        # time:O(N) space:O(N)
        kRet = 0
        cntVisit = 0
        def dfsPreOrder(now):
            nonlocal k, kRet, cntVisit
            if now == None:
                return
            dfsPreOrder(now.left)
            cntVisit+=1
            if cntVisit == k:
                kRet = now.val
                return
            dfsPreOrder(now.right)
        dfsPreOrder(root)
        return kRet
