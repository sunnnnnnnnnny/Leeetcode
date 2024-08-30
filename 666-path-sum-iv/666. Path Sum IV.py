class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # ascending order having the node as pre-order sequence
        # thus going through the list with depth by depth, 
        # we can calculate the prefix of each child's parent path cost
        # by index of level//2+1
        # time:O(N) size of list, space: O(N) or O(1) as each depth parent prefix
        curDepth = 1
        prefix = [0]*9
        nextPrefix = [0]*9
        ret = 0
        def getLeavePathCost(prefix, nextPrefix):
            lastDepthLeaveCost = 0
            for i in range(len(prefix)):
                if prefix[i]>0:
                    # left, right child idx
                    left = (i-1)*2+1
                    right = (i-1)*2+2
                    if nextPrefix[left]==0 and nextPrefix[right]==0:
                        lastDepthLeaveCost+= prefix[i]
            return lastDepthLeaveCost
        def extractNode(nodeN):
            depth = nodeN//100
            level = (nodeN%100)//10
            val = (nodeN%10)
            return depth, level, val
        for node in nums:
            d, l, v = extractNode(node)
            if d != curDepth and d>1:
                curDepth = d
                # compare if any leave node in previous part
                ret += getLeavePathCost(prefix, nextPrefix)
                prefix = copy.deepcopy(nextPrefix)
                nextPrefix = [0]*9
            parent = (l-1)//2+1
            cost = prefix[parent]+v
            nextPrefix[l] = cost
            # print(node, cost, prefix)
        # only the leave path cost
        # print(nextPrefix)
        ret += getLeavePathCost(prefix, nextPrefix)
        for c in nextPrefix:
            ret += c
        return ret


        