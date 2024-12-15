# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # make the in order traversal will get ordered numbr
        # then by 2 pointers we can check it
        # time: O(2N) space:O(N)
        num = []
        def bfs(now):
            nonlocal num
            if now == None:
                return
            bfs(now.left)
            num.append(now.val)
            bfs(now.right)
        bfs(root)
        l = 0
        r = len(num)-1
        # print(num)
        while l<r:
            nowSum  = num[l]+num[r]
            if nowSum==k:
                return True
            elif nowSum>k:
                r -= 1
            else:
                l+=1
        return False