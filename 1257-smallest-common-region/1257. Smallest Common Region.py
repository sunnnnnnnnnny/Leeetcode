class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # LCA where we can build a tree based on regions
        # time:O(E+N) with buildig the tree and doing dfs
        # space:O(N)
        # record the indegree and connection
        node = {}
        for r in regions:
            parent = r[0]
            for child in range(1, len(r)):
                node[r[child]] = parent
        # print(node)
        r1Par = set()
        nextPar = region1
        while nextPar in node.keys():
            r1Par.add(nextPar)
            nextPar = node[nextPar]
        
        nextPar = region2
        while nextPar in node.keys():
            if nextPar in r1Par:
                return nextPar
            nextPar = node[nextPar]
        return nextPar

