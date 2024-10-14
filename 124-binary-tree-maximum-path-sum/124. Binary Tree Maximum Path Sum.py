# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # traverse the whole tree and get the result of left child sum, right child path, sum of left+right+self
        # return the max(self, self+max(left, right))
        # time:O(N) space:O(N)
        if root == None:
            return 0
        
        maxPath = root.val
        if root.left!= None:
            maxPath+=root.left.val
        elif root.right!= None:
            maxPath+=root.right.val
        def postOrder(now):
            nonlocal maxPath
            if now == None:
                return 0
            leftPath = postOrder(now.left)
            rightPath = postOrder(now.right)
            childMax = max(leftPath, rightPath)
            curMax = max(leftPath+rightPath, childMax)
            # need path to be consider but may have different idea?
            # if now.left != None or now.right != None:
            #     maxPath = max(maxPath, curMax+now.val)
            # print(now.val, leftPath, rightPath,curMax )
            # if self can be consider
            curMax = max(0, curMax)
            maxPath = max(maxPath, curMax+now.val)
            childMax = max(childMax+now.val, now.val)
            return childMax
        postOrder(root)
        return maxPath

        