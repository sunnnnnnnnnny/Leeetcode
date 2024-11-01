class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        n = len(price)
        ret = 0
        # dp = [[0]*(maxCoupons+1)]*(maxAmount+1)
        # without memo, time:O(2^n)
        @cache
        def bkV1(idx, leftAmount, leftCoupon):
            nonlocal n, ret, price, tastiness
            if idx == n:
                return 0
            nowMax = 0
            nowMax = max(nowMax, bkV1(idx+1, leftAmount, leftCoupon))
            if price[idx]<=leftAmount:
                nowMax = max(nowMax,tastiness[idx]+bkV1(idx+1, leftAmount-price[idx], leftCoupon))
            
            if price[idx]//2<=leftAmount and leftCoupon>0:
                nowMax = max(nowMax,tastiness[idx]+bkV1(idx+1, leftAmount-(price[idx]//2), leftCoupon-1))
            
            return nowMax
        ret = bkV1(0,maxAmount, maxCoupons)
        # def bk(idx, curTaste, leftAmount, leftCoupon):
        #     nonlocal n, ret, price, tastiness
        #     if idx == n:
        #         return 0
        #     nowMax = 0
        #     if price[idx]<=leftAmount:
        #         nowMax = max(nowMax,tastiness[idx]+bk(idx+1, curTaste+tastiness[idx], leftAmount-price[idx], leftCoupon))
            
        #     if price[idx]//2<=leftAmount and leftCoupon>0:
        #         nowMax = max(nowMax,tastiness[idx]+bk(idx+1, curTaste+tastiness[idx], leftAmount-(price[idx]//2), leftCoupon-1))
            
        #     nowMax = max(nowMax, bk(idx+1, curTaste, leftAmount, leftCoupon))
        #     # dp[leftAmount][leftCoupon] = nowMax
        #     return nowMax
        # ret = bk(0,0, maxAmount, maxCoupons)
        # print(dp)
        return ret