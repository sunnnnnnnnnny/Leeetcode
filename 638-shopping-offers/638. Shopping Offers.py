class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # the key is the item needed, we try all the special until we can't find any
        # time:O(M*N) space:O(M*N)
        memo = {}
        n = len(price)
        def bk(leftItems):
            nonlocal price, special, memo, n
            needItems = 0
            minP = 0
            for i in range(n):
                if leftItems[i]>0:
                    needItems+=1
                    minP += price[i]*leftItems[i]
            if needItems == 0:
                return 0
            if tuple(leftItems) in memo.keys():
                return memo[tuple(leftItems)]
            for s in special:
                sAllow = True
                newLeft = list(leftItems)
                for i in range(n):
                    newLeft[i] = leftItems[i]-s[i]
                    if newLeft[i]<0:
                        sAllow = False
                        break
                if sAllow:
                    pNow = bk(newLeft)+s[-1]
                    minP = min(minP, pNow)
            memo[tuple(leftItems)] = minP
            return minP
        return bk(needs)
