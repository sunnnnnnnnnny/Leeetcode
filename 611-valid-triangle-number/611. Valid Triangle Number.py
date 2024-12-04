class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # valid triangle would be small side sum>largest side
        # since we are treating same val different index as result
        # we can sort the array from small to large
        # then pick the first 2 num, and dirctly getting the possible large side
        # time:O(NlogN+N^3) space:O(N)
        # if we get the thrid side with binary search
        nums.sort()
        n = len(nums)
        ret = 0
        for f in range(n-2):
            for s in range(f+1, n-1):
                largeS = nums[f]+nums[s]
                tIdx = bisect.bisect_left(nums, largeS)
                # print(tIdx, largeS)
                if tIdx>s and nums[tIdx-1]<largeS:
                    ret += tIdx-s-1
                # for t in range(s+1, n):
                #     if nums[t]<largeS:
                #         ret += 1
                #     else:
                #         break
        return ret