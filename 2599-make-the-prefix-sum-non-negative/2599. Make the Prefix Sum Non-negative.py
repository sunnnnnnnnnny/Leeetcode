class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        # by recording the neg num and get the smallest to end by minHeap
        # time: O(NlogN) space:O(N) assume M max swap
        negHeap = []
        prefixSum = 0
        swap = 0
        for n in nums:
            if n>=0:
                prefixSum += n
            else:
                prefixSum+=n
                heapq.heappush(negHeap, n)
                if prefixSum<0:
                    smallestN = heapq.heappop(negHeap)
                    prefixSum -= smallestN
                    swap += 1
                
        return swap

        