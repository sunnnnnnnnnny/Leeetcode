class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of the min from left
        # moving to right we can always get the max profit of the current moment
        # time:O(N) space:O(1) cause we only need to keep track of the current min
        nowMin = prices[0]
        allMax = 0
        for i in range(1, len(prices)):
            curProfit = prices[i]-nowMin
            allMax = max(allMax, curProfit)
            nowMin = min(nowMin, prices[i])
        return allMax