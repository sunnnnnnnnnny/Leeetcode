# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do the in-order traversal and always dfs to left tree
        # as bst is left<root<right
        # time:O(N) space:O(N)
        kthSmall = -1
        def dfsBst(rootSmall:int, now: Optional[TreeNode]):
            nonlocal kthSmall
            if now == None:
                return rootSmall
            if kthSmall >=0:
                return rootSmall
            leftSmall = dfsBst(rootSmall, now.left)
            nowSmall = leftSmall+1
            # print(now)
            # print(leftSmall)
            if nowSmall == k:
                kthSmall = now.val
                return nowSmall

            rightSmall = dfsBst(nowSmall, now.right)
            return rightSmall
        dfsBst(0, root)
        return kthSmall
        