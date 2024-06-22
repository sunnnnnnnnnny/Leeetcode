# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # time: O(N)
        # space:O(N)
        ans =[]
        # def dfs(cur):
        #     if cur == None:
        #         return []
        #     left = dfs(cur.left)
        #     right = dfs(cur.right)
        #     return left+[cur.val]+right
        def dfsToAns(cur):
            if cur == None:
                return 
            left = dfsToAns(cur.left)
            ans.append(cur.val)
            right = dfsToAns(cur.right)
        dfsToAns(root)
        return ans
        