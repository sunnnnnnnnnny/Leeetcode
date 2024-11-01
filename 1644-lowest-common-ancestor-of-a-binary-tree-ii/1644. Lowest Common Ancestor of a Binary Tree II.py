# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # record the path to p, then while looking for q the first common parent is LCA
        # time:O(2N) space:O(2N) with saving the path and recursive
        ret = None
        lookPar = set()
        def dfsFind(now, parents, target):
            nonlocal lookPar, ret
            if now == None:
                return False
            if now.val == target.val:
                if len(lookPar) == 0:
                    lookPar.add(now.val)
                    for p in parents:
                        lookPar.add(p.val)
                    return True
                # LCA look from the lowest level
                if now.val in lookPar:
                    ret = now
                    return True
                for i in range(len(parents)-1, -1, -1):
                    nowVal = parents[i].val
                    if nowVal in lookPar:
                        ret = parents[i]
                        return True
                return False
            parents.append(now)
            dfsFind(now.left, parents, target)
            dfsFind(now.right, parents, target)
            parents.pop()
            return False
        dfsFind(root, [], p)
        if len(lookPar)==0:
            # p not found
            return None
        dfsFind(root, [], q)
        return ret
