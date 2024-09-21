class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # binary tree can store these information with LCA will find the information
        # by dfs with post order travesal
        # O(N) N is regions count space:O(N)
        # search from child to parent, time:O(N) space:O(N)
        region2Includ = {}
        for reg in regions:
            par = reg[0]
            for i in range(1, len(reg)):
                region2Includ[reg[i]] = par
            
        if region1 not in region2Includ.keys():
            return ""
        if region2 not in region2Includ.keys():
            return ""
        visitedPar = set()
        now1 = region1
        now2 = region2
        while len(now1)>0 or len(now2)>0:
            if len(now1)>0 and now1 in visitedPar:
                return now1
            visitedPar.add(now1)
            if len(now2)>0 and now2 in visitedPar:
                return now2
            visitedPar.add(now2)
            if now1 in region2Includ.keys():
                now1 = region2Includ[now1]
            else:
                now1 = ""
            if now2 in region2Includ.keys():
                now2 = region2Includ[now2]
            else:
                now2 = ""
        return ""