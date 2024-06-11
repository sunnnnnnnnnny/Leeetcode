class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through the list one by one with keep record of the top K freq items
        # by having the  top k freq cnt, if any item exceed that then we exchange
        # with adding it to the cnt then remove the least freq in top k list
        # time:O(N+MlogK) M is the unique nums as we do at most M pop
        # M is <= N
        # space:O(3N)  = O(N)
        numToFreq = collections.Counter(nums)
        freqToNum = {}
        topKQueue = []
        for num, freq in numToFreq.items():
            if freq not in freqToNum.keys():
                freqToNum[freq] = []
            freqToNum[freq].append(num)
            if len(topKQueue)<k:
                heapq.heappush(topKQueue, freq)
            else:
                if topKQueue[0]<freq:
                    heapq.heappop(topKQueue)
                    heapq.heappush(topKQueue, freq)
        ans = []
        while len(topKQueue)>0:
            freq = heapq.heappop(topKQueue)
            if freq in freqToNum.keys():
                ans += freqToNum[freq]
                del freqToNum[freq]
        return ans




        