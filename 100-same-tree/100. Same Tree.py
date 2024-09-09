# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print as preorder traversal with none child as #
        # then make string compare
        # N is tree p size, M is tree q size
        # time:O(N+M+ max(N,M)) the max(N,M) is the string compare time
        # space:O(N+M)
        def preOrderStr(now, nowStr):
            if now == None:
                return nowStr+"#"
            nextStr = nowStr+str(now.val)
            nextStr = preOrderStr(now.left, nextStr)
            return preOrderStr(now.right, nextStr)
        pStr = preOrderStr(p, "")
        qStr = preOrderStr(q, "")
        return pStr == qStr