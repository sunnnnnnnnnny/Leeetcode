# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # the parent node should be the middle one of the 
        # then we can recursively getting the height balance tree
        # time:O(N) space:O(N)
        def buildMid(startI, endI):
            nonlocal nums
            if startI>endI:
                return None
            if startI == endI:
                return TreeNode(nums[startI])
            mid = (startI+endI)//2
            par = TreeNode(nums[mid])
            par.left = buildMid(startI, mid-1)
            par.right = buildMid(mid+1, endI)
            return par
        return buildMid(0, len(nums)-1)
