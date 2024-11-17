class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # finding the window with least unique flavor
        # sliding window with k size
        uniqFlav= len(set(candies))
        n = len(candies)
        totalFlavor = collections.Counter(candies)
        for i in range(k):
           totalFlavor[candies[i]]-=1
           if totalFlavor[candies[i]] == 0:
            uniqFlav-=1
        maxCnt = uniqFlav
        start = 0
        if k>0:
            for i in range(k,n):
                totalFlavor[candies[i]]-=1
                totalFlavor[candies[start]]+=1
                if totalFlavor[candies[i]] == 0:
                    uniqFlav-=1
                if candies[start]!=candies[i] and totalFlavor[candies[start]] == 1:
                    uniqFlav+=1
                start +=1
                maxCnt = max(maxCnt,uniqFlav)
        return maxCnt


