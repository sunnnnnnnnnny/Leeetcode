class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # dp[i][j] = all x<i with dp[x][j], all x<i-2 min(dp[x][j-1],nums[i])
        # bk time:O(n*k)
        # binary search with condition of having at most k below num
        # time:O(NlogM) where M is max(nums)-min(nums)
        l = min(nums)
        r = max(nums)
        n= len(nums)
        def haveK(numCheck):
            nonlocal nums, k, n
            cnt = 0
            i=0
            while i<n:
                if nums[i]<numCheck:
                    cnt +=1
                    if cnt>=k:
                        return True
                    i+=2
                else:
                    i+=1
            return False

        while l<=r:
            mid = (l+r)//2
            if haveK(mid):
                r = mid-1
            else:
                l = mid+1
        return r
        # memo = {}
        # n = len(nums)
        # def bk(nowLeftCnt, idx):
        #     nonlocal nums, k, n, memo
        #     if nowLeftCnt==0:
        #         return 0
        #     if idx>=n:
        #         return max(nums)
        #     if (idx, nowLeftCnt) in memo:
        #         return memo[(idx, nowLeftCnt)]
        #     # print(idx, nowLeftCnt)
        #     dontTake = bk(nowLeftCnt, idx+1)

        #     takeNum = max(nums[idx],bk( nowLeftCnt-1, idx+2))
        #     nowRet = min(dontTake, takeNum)
        #     memo[(idx, nowLeftCnt)] = nowRet
        #     return nowRet
        # return bk(k,0)