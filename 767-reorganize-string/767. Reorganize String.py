class Solution:
    def reorganizeString(self, s: str) -> str:
        # as long as the top freq character<all other character sum
        # b/c we need to fill the gap of the max character, n-1 gap
        # first calculate the frequency, then put into priority queue
        #  to put the chars, always put the largest 2 char
        # time:O(N+KLogK+K) k is the unique character space:O(K)
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq.keys():
                freq[s[i]] = 0
            freq[s[i]] += 1
        pq= []
        for k,v in freq.items():
            heapq.heappush(pq, (-v, k))
        topF, topK = pq[0]
        # not possible to get such result
        if -topF-1>len(s)+topF:
            return ""
        ret = ""
        while len(pq)>0:
            oneF, oneK = heapq.heappop(pq)
            ret+=oneK
            newOneF = -oneF-1
            if len(pq)>0:
                twoF, twoK = heapq.heappop(pq)
                ret+=twoK
                newTwoF = -twoF-1
                if newTwoF>0:
                    heapq.heappush(pq, (-newTwoF, twoK))
            if newOneF>0:
                heapq.heappush(pq, (-newOneF, oneK))
        return ret
