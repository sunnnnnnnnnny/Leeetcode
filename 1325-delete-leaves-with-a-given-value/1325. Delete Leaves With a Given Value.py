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
        # Space: O(N) as the call stack will be used
        def getChild(now: Optional[TreeNode]):
            if now == None:
                return now
            now.left = getChild(now.left)
            now.right = getChild(now.right)
            if now.left == None and now.right == None:
                if now.val == target:
                    return None
            return now
        
        newRoot = getChild(root)
        return newRoot

        