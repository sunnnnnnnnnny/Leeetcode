# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # do dfs post order traversal and return the deepest child and the LCA
        # merge if needed
        # time:O(N) space:O(N)
        def postDfs(now, parent, depth):
            if now == None:
                return depth, parent
            leftDep, leftLca = postDfs(now.left, now, depth+1)
            rightDep, rightLca = postDfs(now.right, now, depth+1)
            if leftDep>rightDep:
                return leftDep, leftLca
            elif leftDep<rightDep:
                return rightDep, rightLca
            else:
                return leftDep, now
        def bfsSubTree(startN):
            bfsQ = [startN]
            ret = []
            while bfsQ:
                sL = len(bfsQ)
                for i in range(sL):
                    now = bfsQ.pop(0)
                    ret.append(now)
                    if now.left:
                        bfsQ.append(now.left)
                    if now.right:
                        bfsQ.append(now.right)
            return ret
        dep, lca = postDfs(root, None, 0)
        if lca== None:
            return None
        
        # print(dep, lca.val)
        return lca
        # realret = bfsSubTree(lca)
        # print(len(realret))
        # return realret

        