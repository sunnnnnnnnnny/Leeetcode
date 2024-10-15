class Solution:
    def reorganizeString(self, s: str) -> str:
        # as long as the top freq character<all other character sum
        # b/c we need to fill the gap of the max character, n-1 gap
        # first calculate the frequency, then put into priority queue
        #  to put the chars, always put the largest 2 char
        # time:O(N+KLogK+K) k is the unique character space:O(K)
        # use the freq to put the char, based on the even location then the odd
        # time:O(N) space:O(K)
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq.keys():
                freq[s[i]] = 0
            freq[s[i]] += 1
        maxEle = 0
        letter = ''
        for k,v in freq.items():
            if v>maxEle:
                maxEle = v
                letter = k
        if maxEle-1>len(s)-maxEle:
            return ""
        ret = [" " for i in range(len(s))]
        idx = 0
        while freq[letter]>0:
            ret[idx] = letter
            idx += 2
            freq[letter] -= 1
        for k,v in freq.items():
            while v>0:
                # print(k,v,ret)
                if idx>=len(s):
                    idx = 1
                ret[idx] = k
                idx += 2
                v -=1
        return "".join(ret)
        # pq= []
        # for k,v in freq.items():
        #     heapq.heappush(pq, (-v, k))
        # topF, topK = pq[0]
        # # not possible to get such result
        # if -topF-1>len(s)+topF:
        #     return ""
        # ret = ""
        # while len(pq)>0:
        #     oneF, oneK = heapq.heappop(pq)
        #     ret+=oneK
        #     newOneF = -oneF-1
        #     if len(pq)>0:
        #         twoF, twoK = heapq.heappop(pq)
        #         ret+=twoK
        #         newTwoF = -twoF-1
        #         if newTwoF>0:
        #             heapq.heappush(pq, (-newTwoF, twoK))
        #     if newOneF>0:
        #         heapq.heappush(pq, (-newOneF, oneK))
        # return ret
