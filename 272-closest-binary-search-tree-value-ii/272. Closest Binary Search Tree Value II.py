# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # maxStack of size K to keep record of the dist, val
        # or using the BST with pre-order then we can get the k
        # time:O(N) space:O(N)
        ret = []
        def inOrder(now):
            nonlocal target, ret,k
            if now == None:
                return
            inOrder(now.left)
            nowDist = abs(now.val-target)
            # print(now.val, nowDist)
            if len(ret)>=k:
                maxDist, val = ret[0]
                # print(now.val, maxDist, val)
                if nowDist<-maxDist:
                    heapq.heappop(ret)
                    heapq.heappush(ret, (-nowDist, now.val))
            else:
                heapq.heappush(ret, (-nowDist, now.val))
            inOrder(now.right)
        inOrder(root)
        ans = []
        while ret:
            dist, num = heapq.heappop(ret)
            ans.append(num)
        return ans
