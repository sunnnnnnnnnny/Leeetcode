# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # make bfs traversal and check each level having the 2^level nodes from left to right
        # level = 0
        if root == None:
            return True
        bfsQ = [root]
        while bfsQ:
            # expectSize = 2*level
            # prevCntPass = (levelS ==expectSize)
            noneExt = False
            haveValidChild = False
            levelS = len(bfsQ)
            for i in range(levelS):
                now = bfsQ.pop(0)
                if now == None:
                    noneExt = True
                else:
                    if noneExt:
                        # non valid node should be after none
                        return False
                    if now.left!=None or now.right!=None:
                        haveValidChild = True
                    bfsQ.append(now.left)
                    bfsQ.append(now.right)
            if noneExt and haveValidChild:
                return False
        return True
