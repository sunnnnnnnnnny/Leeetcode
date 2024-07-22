# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # using the characteristic of BST
        # time:O(N) space:O(N) dfs?
        if root == None:
            return 0
        ret = root.val
        cur = root
        while cur!=None:
            retDiff = abs(ret-target)
            curDiff = abs(cur.val-target)
            # print(ret, cur.val, retDiff, curDiff)
            if retDiff > curDiff:
                ret = cur.val
            elif retDiff == curDiff:
                ret = min(ret, cur.val)
            if cur.val>target:
                cur = cur.left
            elif cur.val<target:
                cur = cur.right
            else:
                return cur.val
        return ret
        