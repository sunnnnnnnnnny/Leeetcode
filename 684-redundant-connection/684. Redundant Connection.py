class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    def find(self, idx):
        if self.par[idx]!=idx:
            self.par[idx] = self.find(self.par[idx])
        return self.par[idx]
    def union(self, a, b):
        aPar = self.find(a)
        bPar = self.find(b)
        if aPar == bPar:
            return True
        # merge to the higher rank one
        if self.rank[aPar]>=self.rank[bPar]:
            self.par[bPar] = aPar
        elif self.rank[aPar]<self.rank[bPar]:
            self.par[aPar] = bPar
        else:
            self.par[bPar] = aPar
            self.rank[aPar] += 1
        return False
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # using union find to check if the edge is needed, by checking
        # the a to b having a connection
        n = len(edges)
        dsu = DSU(n)
        ret = -1
        for i in range(n):
            a, b = edges[i]
            noNeedMerge = dsu.union(a, b)
            if noNeedMerge:
                ret = i
        if ret>=0:
            return edges[ret]
        return []

