# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # (my idea-wrong)transform the tree into graph then get the maxpath?
        # then with a vitual node connecting all node
        # push the max cost to the neighbor
        # considering to split the question into left, left+mid+right, right
        # using pre-order dfs to get the sum of path
        # keep record of maxPath and the tree path
        # time: O(N) space:O(N)
        maxPath = -float("inf")
        def calPath(now: Optional[TreeNode]):
            nonlocal maxPath
            if now == None:
                return 0
            # pre-order
            leftCost = max(calPath(now.left), 0)
            rightCost = max(calPath(now.right), 0)
            # the connected cost to return can't be including both left+right
            # as then it won't be a path to connect the above parent
            connectCost = max(now.val+leftCost, now.val+rightCost)
            # need to avoid the empty child and still keep a path
            # since the cost is max at 0, we always has the root=valid path
            maxPath = max(maxPath, now.val+leftCost+rightCost)
            return connectCost
        calPath(root)
        return maxPath
