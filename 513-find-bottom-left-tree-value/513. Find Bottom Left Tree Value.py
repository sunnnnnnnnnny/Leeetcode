# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # last row is with bfs, and left most would be the first node in that level
        # bfs time:O(N) n is the treenode size spze:O(N)
        ret= -1
        bfsQ = [root]
        while bfsQ:
            levelSize = len(bfsQ)
            for i in range(levelSize):
                now = bfsQ.pop(0)
                if i==0:
                    ret = now.val
                if now.left:
                    bfsQ.append(now.left)
                if now.right:
                    bfsQ.append(now.right)
        return ret