class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # find the one with zero indegree
        # time:O(V+E) space:O(V)
        vNode = [0]*n
        for e in edges:
            f, t = e
            vNode[t] += 1
        ret = []
        for i in range(n):
            if vNode[i] == 0:
                ret.append(i)
        return ret
