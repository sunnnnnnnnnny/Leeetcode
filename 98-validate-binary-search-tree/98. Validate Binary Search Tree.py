# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # using in order traverse to check if the condition is met
        # dfs will cost: time O(N) space O(N) as stack
        # or list the num in inorder traverse
        # then check all numbers are going increasing
        def checkBST(now: Optional[TreeNode], leftBond: Optional[TreeNode], rightBond: Optional[TreeNode]):
            if now == None:
                return True
            if leftBond != None:
                if now.val<=leftBond.val:
                    return False
            if rightBond != None:
                if now.val>=rightBond.val:
                    return False
            if not checkBST(now.left, leftBond, now):
                return False
            if not checkBST(now.right, now, rightBond):
                return False
            return True
        return checkBST(root, None, None)
            
        