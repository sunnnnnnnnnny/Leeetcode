# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # count the depth from leaf, then added them in the ret
        dep2Node = defaultdict(list)
        def dfs(now):
            nonlocal dep2Node
            if now == None:
                return 0
            leftDep = dfs(now.left)+1
            rightDep = dfs(now.right)+1
            nowDep = max(leftDep, rightDep)
            dep2Node[nowDep].append(now.val)
            return nowDep
        maxDep = dfs(root)
        ret = []
        for i in range(1, maxDep+1):
            ret.append(dep2Node[i])
        return ret