# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # pre-order traversal with list size k, as we reached k items 
        # compare to remove the head or the tail
        # time:O(N) space:O(N+N) = O(N)
        kList = []
        def preOrder(now):
            nonlocal kList, target, k
            if now == None:
                return 
            preOrder(now.left)
            kList.append(now.val)
            preOrder(now.right)
        preOrder(root)
        while len(kList) > k:
            headDiff = abs(kList[0]-target)
            tailDiff = abs(kList[-1]-target)
            # print(kList[0], kList[-1], headDiff, tailDiff)
            if headDiff>tailDiff:
                kList.pop(0)
            else:
                kList.pop()
        return kList
