class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force is directly get the rotation point O(N)
        # binary search can get the the min in O(logN)
        # the min would appear in 3 type
        # [0,1,2,3,4], in left=>if right side is sorted and mid>mid-1
        # [4,0,1,2,3] in left=>if right side is sorted and mid>mid-1
        # [2,3,4,0,1] in right=>if left side is sorted and left>right
        theMin = nums[0]
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            theMin = min(theMin, nums[mid])
            if nums[right]>nums[mid]:
                if mid>0 and nums[mid]>nums[mid-1]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[left]>nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        theMin = min(theMin, nums[left])
        return theMin