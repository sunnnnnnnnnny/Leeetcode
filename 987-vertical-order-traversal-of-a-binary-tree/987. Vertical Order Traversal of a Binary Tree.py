# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # record the node's vertical loc and store in the bucket
        # with bfs and priority queue for each bucket
        # time:O(N+NlogN) = O(NlogN) space:O(N)
        if root == None:
            return [[]]
        bfsQ = [(0,0,root)]
        loc2val = defaultdict(list)
        minY = 0
        maxY = 0
        while bfsQ:
            levelSize = len(bfsQ)
            for _ in range(levelSize):
                x,y,now = bfsQ.pop(0)
                minY = min(minY, y)
                maxY = max(maxY, y)
                # heapq.heappush(loc2val[y], now.val)
                loc2val[y].append((x,now.val))
                if now.left:
                    bfsQ.append((x+1,y-1, now.left))
                if now.right:
                    bfsQ.append((x+1,y+1, now.right))
        ret = []
        for i in range(minY, maxY+1):
            loc2val[i].sort(key = lambda x:(x[0], x[1]))

            toRet = [x[1] for x in loc2val[i]]
            # print(i, toRet)
            ret.append(toRet)
        return ret



