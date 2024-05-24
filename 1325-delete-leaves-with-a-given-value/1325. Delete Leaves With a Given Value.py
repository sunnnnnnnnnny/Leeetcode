# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # using dfs traverse the tree, and return the child node for update
        # time: O(N) N is tree nodes
        # Space: O(1) no extra space is needed
        def getChild(now: Optional[TreeNode]):
            if now == None:
                return now
            newLeft = getChild(now.left)
            newRight = getChild(now.right)
            if newLeft == None and newRight == None:
                if now.val == target:
                    return None
            now.left = newLeft
            now.right = newRight
            return now
        
        newRoot = getChild(root)
        return newRoot

        