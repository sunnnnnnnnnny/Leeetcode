# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # with dfs we can get the left and right length of cur
        # compare the max diameter at each node
        # time: O(N) n nodes space:O(N) recursive stack
        maxDia = 0
        def curDiameter(cur):
            nonlocal maxDia
            if cur == None:
                return 0
            leftDia = curDiameter(cur.left)
            rightDia = curDiameter(cur.right)
            maxDia = max(maxDia, leftDia+rightDia)
            return max(leftDia+1, rightDia+1)
        curDiameter(root)
        return maxDia

        