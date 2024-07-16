# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # record the path from root to each node as rlrlrl
        # the distance of p and q will be len(q)+len(q)-2 commonPrefixLen
        if p == q:
            return 0
        tQueue = []
        tQueue.append((root,""))
        pPath = qPath = ""
        while tQueue:
            levelCnt = len(tQueue)
            for _ in range(levelCnt):
                now = tQueue.pop(0)
                nowNode = now[0]
                nowPath = now[1]
                if nowNode.val == p:
                    pPath = nowPath
                elif nowNode.val == q:
                    qPath = nowPath
                if nowNode.left != None:
                    tQueue.append((nowNode.left,nowPath+"l"))
                if nowNode.right != None:
                    tQueue.append((nowNode.right,nowPath+"r"))
            if len(pPath)>0 and len(qPath)>0:
                break
        commonLen  = 0
        # print(pPath, qPath)
        for i in range(min(len(pPath), len(qPath))):
            if pPath[i]!=qPath[i]:
                break
            else:
                commonLen += 1
        # print(commonLen)
        # one path ended earlier
        # if len(pPath)>commonLen and len(qPath)>commonLen and pPath[commonLen]==qPath[commonLen]:
        #     commonLen += 1
        dist = len(pPath)+len(qPath)-2*(commonLen)
        return dist