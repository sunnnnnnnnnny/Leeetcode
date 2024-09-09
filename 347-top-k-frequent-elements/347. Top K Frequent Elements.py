class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort the nums, then by getting the freq also updating the top k freq list (minHeap)
        # time: O(nlogn+nlogK) space:O(N)
        # gothrough the list and count the freq, with minHeap of size k, pop the higher Freq into heap
        # time:O(N*logK+K) space:O(N)
        freq = {}
        for n in nums:
            if n not in freq.keys():
                freq[n] = 0
            freq[n]+=1

        kTopFreq = []
        for key, val in freq.items():
            if len(kTopFreq)<k:
                heapq.heappush(kTopFreq, (val, key))
            else:
                if val>kTopFreq[0][0]:
                    heapq.heappop(kTopFreq)
                    heapq.heappush(kTopFreq, (val, key))
                
        ret = []
        while len(kTopFreq)>0:
            heapMinHeadFreq, heapMinNum = heapq.heappop(kTopFreq)
            ret.append(heapMinNum)
        return ret
