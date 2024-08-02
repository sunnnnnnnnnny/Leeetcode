class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # find the smallest group of 0 to start fill in
        # don't need to care where the 1's are from

        zeroCnt = [0]*(len(nums)+1)
        totalOnes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCnt[i+1] = zeroCnt[i]+1
            else:
                totalOnes+=1
                zeroCnt[i+1] = zeroCnt[i]
        # sliding window for the size of totalOnes
        # the minswap would be the 0 count in the window
        # time: O(N)+O(N) one for getting the zero, one for sliding window
        # spaze:O(N)
        minSwap = -1
        # corner case if no 1
        if totalOnes==0:
            return 0
        end = totalOnes
        for start in range(len(nums)):
            nowZero = 0
            if end>start:
                nowZero = zeroCnt[end]-zeroCnt[start]
            else:
                nowZero = zeroCnt[-1]-zeroCnt[start]+zeroCnt[end]
            # print(start, end, nowZero)
            minSwap = min(minSwap, nowZero) if minSwap>=0 else nowZero
            end = end+1 if end<len(nums) else 1
        return minSwap





        