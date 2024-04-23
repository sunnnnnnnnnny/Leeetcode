class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use array to record the min coin for each number until reach amounts
        # the amount should be min(amount-coin(i))+1
        # assume no dulicate coins and infinite coins
        minCoins = [-1]*(amount+1)
        minCoins[0] = 0
        # getting the assending order is eaiser to check if we need the coin
        coins.sort()
        for i in range(1, amount+1, 1):
            minCoinForI = -1
            for coin in coins:
                if coin>i:
                    break
                elif coin == i:
                    minCoinForI = 1
                    break
                else:
                    prevIdx = i-coin
                    if prevIdx>=0 and minCoins[prevIdx]>0:
                        minCoinForI = min(minCoinForI, minCoins[prevIdx]+1) if(minCoinForI>0) else minCoins[prevIdx]+1
            minCoins[i] = minCoinForI
        return minCoins[amount]

        