# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs with each layer at different index, odd, even
        # time:O(N) space:O(N) for queue
        if root == None:
            return []
        bfsQueue = []
        bfsQueue.append((root, 0))
        ret = [[]]
        startX = 0
        while bfsQueue:
            levelCnt = len(bfsQueue)
            for i in range(levelCnt):
                cur = bfsQueue.pop(0)
                nodeX = cur[1]
                # add one array ret
                actualIdx = nodeX-startX
                if actualIdx<0:
                    newArr = [cur[0].val]
                    ret.insert(0, newArr)
                    startX = nodeX
                elif actualIdx>=len(ret):
                    newArr = [cur[0].val]
                    ret.append(newArr)
                else:
                    ret[actualIdx].append(cur[0].val)
                if cur[0].left != None:
                    bfsQueue.append((cur[0].left, nodeX-1))
                if cur[0].right != None:
                    bfsQueue.append((cur[0].right, nodeX+1))

        return ret



        