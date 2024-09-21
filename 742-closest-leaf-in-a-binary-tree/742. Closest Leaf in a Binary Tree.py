# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # since all node val is unique, we can use dfs with post order traversal
        # and caculate the min dis of each child to leaf
        # time:O(2N) =O(N) space:O(N)
        ret = -1
        val2Dist = {}
        def dfs(now, k):
            nonlocal ret, val2Dist
            if now == None:
                return -1,-1
            if now.left == None and now.right == None:
                val2Dist[now.val] = (0,now.val)
                if now.val == k:
                    ret = now.val 
                return 0,now.val
            leftDist, lNodeVal  = dfs(now.left, k)
            rightDist, rNodeVal = dfs(now.right,k)
            selfDist = min(leftDist, rightDist)+1
            closeNode = lNodeVal if leftDist<rightDist else rNodeVal
            if leftDist<0 or rightDist<0:
                selfDist = rightDist+1 if leftDist<0 else leftDist+1
                closeNode = rNodeVal if leftDist<0 else lNodeVal
            # print(now.val,leftDist,  rightDist, closeNode)

            val2Dist[now.val] = (selfDist,closeNode)
            # if now.val == k:
            #     ret = closeNode 
            return selfDist, closeNode
        if ret > 0:
            return ret
        dfs(root, k)

        def dfsForParDist(now, par, parDist, parLeaf, k):
            nonlocal ret, val2Dist
            if now == None:
                return
            
            childDist, childVal = val2Dist[now.val]
            minLeafDist = min(childDist, parDist+1)
            minLeafVal = childVal if parDist+1>childDist else parLeaf
            if par == None:
                if now.val == k:
                    ret = val2Dist[now.val][1]
                    return
                minLeafDist = val2Dist[now.val][0]
                minLeafVal = val2Dist[now.val][1]
            if now.val == k:
                ret = minLeafVal
                return
            dfsForParDist(now.left, now, minLeafDist, minLeafVal, k)
            dfsForParDist(now.right, now, minLeafDist, minLeafVal, k)
            # print(now.val, minLeafDist, minLeafVal)

            return
        dfsForParDist(root, None, -1, -1, k)
        return ret