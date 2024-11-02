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
        # time:O(N) space:O(N+K)
        ret = []
        def inOrder(now):
            nonlocal target, ret,k
            if now == None:
                return
            inOrder(now.left)
            ret.append(now.val)
            if len(ret)>k:
                head = abs(ret[0]-target)
                last = abs(ret[-1]-target)
                # print(now.val, maxDist, val)
                # if the last distance is further than the first, then any of the is going to be bigger
                # thus we can skip it
                if last>head:
                    ret.pop()
                    return
                else:
                    ret.pop(0)
            inOrder(now.right)
        inOrder(root)
        # ans = []
        # while ret:
        #     dist, num = heapq.heappop(ret)
        #     ans.append(num)
        return ret
