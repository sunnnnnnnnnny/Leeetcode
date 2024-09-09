# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs traversal the tree
        # time: O(N) spcae:O(N)
        bfsQ = []
        ret = []
        if root == None:
            return ret
        bfsQ.append(root)
        while bfsQ:
            levelS = len(bfsQ)
            nowLevelRet = []
            for i in range(levelS):
                now = bfsQ.pop(0)
                nowLevelRet.append(now.val)
                if now.left != None:
                    bfsQ.append(now.left)
                if now.right != None:
                    bfsQ.append(now.right)
            ret.append(nowLevelRet)
        return ret