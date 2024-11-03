# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # count the level from the end, then add them 
        retList = []
        def dfs(now):
            nonlocal retList
            if now == None:
                return -1
            lEnd = dfs(now.left)
            rEnd = dfs(now.right)
            nowEnd = max(lEnd, rEnd)+1
            if nowEnd == len(retList):
                retList.append([now.val])
            else:
                retList[nowEnd].append(now.val)
            return nowEnd
        maxLen = dfs(root)
        # ret = []
        # for x in retList:
        #     ret.extend(x)
        return retList

