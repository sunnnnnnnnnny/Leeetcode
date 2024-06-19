class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # easier understanding is to find the min Price upto current point
        minPrice = prices[0]
        maxProfit = 0
        for end in range(len(prices)):
            maxProfit = max(maxProfit, prices[end]-minPrice)
            minPrice = min(minPrice, prices[end])
        return maxProfit
        # find the max diff from prev to current
        # shrisk the start if the no profit ending on day end
        # time: O(N) space:O(1)
        # start = 0
        # maxProfit = 0
        # curProfit = 0
        # for end in range(len(prices)):
        #     curProfit = prices[end]-prices[start]
        #     while curProfit<0:
        #         start += 1
        #         curProfit = prices[end]-prices[start]
        #     maxProfit = max(maxProfit, curProfit)
        # return maxProfit
        