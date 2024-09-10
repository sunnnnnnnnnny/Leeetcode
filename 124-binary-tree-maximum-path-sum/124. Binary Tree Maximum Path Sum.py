# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # assume the path needs to be link by leaf node?
        # then with returning the maxPath of left and righ child
        # we can get the max of any node that's connected
        # with postorder traversal time:O(N) space:O(N)
        maxPathCost = -inf
        def dfsCost(now):
            nonlocal maxPathCost
            if now == None:
                return 0
            leftChildCost = dfsCost(now.left)
            rightChildCost = dfsCost(now.right)
            totalCost = now.val+leftChildCost+rightChildCost
            maxNowCost = max(totalCost, now.val)
            maxNowCost = max(maxNowCost, max(leftChildCost,rightChildCost)+now.val)
            maxPathCost = max(maxPathCost, maxNowCost)
            return max(0, max(leftChildCost,rightChildCost))+now.val
        dfsCost(root)
        return maxPathCost
