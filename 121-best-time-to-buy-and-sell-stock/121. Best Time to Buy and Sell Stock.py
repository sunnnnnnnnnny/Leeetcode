class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want to find the min of left max of right
        # using prefix array to record the min n from left, 
        # and max n from the right. 
        # thus at each point we get the max gain at each location
        # time: O(2n) space:O(n)
        lMin = [0]*len(prices)
        lMin[0] = prices[0]
        for i in range(1, len(prices)):
            lMin[i] = min(lMin[i-1], prices[i])
        maxR = prices[-1]
        maxGain = 0
        for i in range(len(prices)-1, -1,-1):
            maxR = max(maxR, prices[i])
            maxGain = max(maxGain, maxR-lMin[i])
        
        return maxGain