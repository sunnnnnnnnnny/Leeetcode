class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 2 binary search for one to get the start, one to get the end
        # time:O(2LogN) space:O(1)
        def startSearch(tar, nums, l, r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == tar and ((mid>0 and nums[mid-1]<nums[mid]) or mid == 0):
                    return mid
                if nums[mid]>=tar:
                    r = mid-1
                else:
                    l = mid+1
            return l
        def endSearch(tar, nums, l, r, end):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == tar and ((mid<end and nums[mid+1]>nums[mid]) or mid == end):
                    return mid
                if nums[mid]<=tar:
                    l = mid+1
                else:
                    r = mid-1
            return r
        end = len(nums)-1
        if end < 0:
            return [-1,-1]
        start = startSearch(target, nums, 0, end)
        # print(start)
        if start<0 or start>end or target != nums[start]:
            return [-1, -1]
        end = endSearch(target, nums, start, end, end)
        return [start, end]