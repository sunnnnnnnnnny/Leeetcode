# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs traverse the tree
        # time: O(N) space: O(N) N is node size
        if root == None:
            return 0
        def getLevel(cur: Optional[TreeNode]) -> int:
            if cur == None:
                return 0
            curLevelLeft = getLevel(cur.left)
            curLevelRight = getLevel(cur.right)
            curLevel = max(curLevelLeft, curLevelRight)+1   
            return curLevel 
        return getLevel(root)
         