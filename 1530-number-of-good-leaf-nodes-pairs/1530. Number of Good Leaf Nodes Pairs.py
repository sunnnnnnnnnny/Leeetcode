# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # by recording the count of leaf node to dist at each parent node
        # we can get the shorest dist of each pair
        # time:O(N) dfs all tree
        # space:O(N) to record the count to dist
        ret = 0
        def leafDist2Count(now):
            nonlocal ret
            if now == None:
                return {}
            dist2Leaf = {}
            left = leafDist2Count(now.left)
            right = leafDist2Count(now.right)
            if len(left) == 0 and len(right) == 0:
                dist2Leaf[0]=1
            else:
                for distl, cntl in left.items():
                    # shorest path is less or equal to distance
                    need = distance-distl-1
                    if need <1:
                        continue
                    for i in range(need):
                        if i in right.keys():
                            pairCnt = right[i]*cntl
                            ret += pairCnt
                # update the child
                for distl, cntl in left.items():
                    newKey = distl+1 if distl<=distance else distance
                    dist2Leaf[newKey] = cntl
                for distr, cntr in right.items():
                    newKey = distr+1 if distr<=distance else distance
                    if newKey not in dist2Leaf.keys():
                        dist2Leaf[newKey] = 0
                    dist2Leaf[newKey] += cntr
            return dist2Leaf
        allLeft2Dist = leafDist2Count(root)
        print(allLeft2Dist)
        return ret

        