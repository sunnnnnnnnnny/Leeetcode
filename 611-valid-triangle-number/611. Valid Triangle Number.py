class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # valid triangle would be small side sum>largest side
        # since we are treating same val different index as result
        # we can sort the array from small to large
        # then pick the first 2 num, and dirctly getting the possible large side
        # time:O(NlogN+N^3) space:O(N)
        # if we get the thrid side with binary search time:O(N^2logN)
        nums.sort()
        n = len(nums)
        ret = 0
        # for moving j and k at most n in the for, time:O(NlogN+N^2)
        # space:O(N) for sorting
        for f in range(n-2):
            k = f+2
            if nums[f]==0:
                continue
            for j in range(f+1, n-1):
                while k<n and nums[f]+nums[j]>nums[k]:
                    k+=1
                ret += k-j-1
        
        # for f in range(n-2):
        #     for s in range(f+1, n-1):
        #         largeS = nums[f]+nums[s]
        #         tIdx = bisect.bisect_left(nums, largeS)
        #         # print(tIdx, largeS)
        #         if tIdx>s and nums[tIdx-1]<largeS:
        #             ret += tIdx-s-1
        return ret