class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp
        coins.sort()
        cnt = [-1]*(amount+1)
        cnt[0] = 0
        for i in range(1, amount+1):
            minWay = -1
            for c in coins:
                left = i-c
                if left>=0 and cnt[left]>=0:
                    nowWay = cnt[left]+1
                    minWay = min(minWay, nowWay) if minWay>0 else nowWay
            cnt[i] = minWay
        return cnt[amount]
