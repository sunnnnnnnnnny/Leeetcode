class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # the score of each node would be size_leftChild*size_rightChild*size_parent
        # the size of the parent would be the rest of the child+1
        # record the childs, and each node's child size
        # time: O(N) space:O(N)
        n = len(parents)
        childs = [[]for _ in range(n)]
        nodeSubtreeSize = [0 for _ in range(n)]
        for i in range(1,n):
            childs[parents[i]].append(i)
        # print(childs)
        def dfs(now):
            nonlocal childs, nodeSubtreeSize
            childSize = 0
            for nextIdx in childs[now]:
                childSize += dfs(nextIdx)
            nodeSubtreeSize[now] = childSize+1
            return nodeSubtreeSize[now]
        wholeTreeSize = dfs(0)
        nowMax = 1
        for ch in childs[0]:
            nowMax *= nodeSubtreeSize[ch]
        ret = [0]
        for i in range(1,n):
            nowScore = wholeTreeSize-nodeSubtreeSize[i]
            for ch in childs[i]:
                nowScore *= nodeSubtreeSize[ch]
            if nowScore>nowMax:
                ret = [i]
                nowMax = nowScore
            elif nowScore == nowMax:
                ret.append(i)
        return len(ret)
            
            
                