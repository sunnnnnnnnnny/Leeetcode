class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search
        def leftSearch(tar, l, r, nlist):
            while l<=r:
                mid = (l+r)//2
                if nlist[mid]>=tar:
                    r = mid-1
                else:
                    l = mid+1
            return l
        
        def rightSearch(tar, l, r, nlist):
            while l<=r:
                mid = (l+r)//2
                if nlist[mid]<=tar:
                    l=mid+1
                else:
                    r = mid-1
            return r
        n = len(nums)
        start = leftSearch(target, 0, n-1, nums)
        # print(start, n)
        if start<0 or start>=n or nums[start]!=target:
            return [-1, -1]
        end = rightSearch(target, start, n-1, nums)
        return [start, end]