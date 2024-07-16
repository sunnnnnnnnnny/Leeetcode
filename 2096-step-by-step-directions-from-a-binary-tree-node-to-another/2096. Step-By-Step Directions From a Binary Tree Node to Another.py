# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find the LCA and the shorest path to s and t from root
        # then the shortest path will be s->LCA->t
        # time:O(N) space:O(1) string recording
        sPath = tPath = ""
        bfs = [(root,"")]
        while bfs:
            levelCnt = len(bfs)
            for _ in range(levelCnt):
                now, path = bfs.pop(0)
                if now.val == startValue:
                    sPath = path
                if now.val == destValue:
                    tPath = path
                if now.left != None:
                    bfs.append((now.left, path+"L"))
                if now.right != None:
                    bfs.append((now.right, path+"R"))
            if len(sPath)>0 and len(tPath)>0:
                break
        lcaLen = 0
        for i in range(min(len(sPath), len(tPath))):
            if sPath[i]!=tPath[i]:
                break
            else:
                lcaLen+=1
        ret = ("U")*(len(sPath)-lcaLen)
        for i in range(lcaLen, len(tPath)):
            ret += tPath[i]
        return ret
        