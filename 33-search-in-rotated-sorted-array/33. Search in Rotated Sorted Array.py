class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search with shifted address
        # time: O(logn) space:O(1)
        left = 0
        right = len(nums)-1
        n = len(nums)-1
        while left<right:
            mid = (left+right)//2
            print(left, right, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                # left side is sorted
                if nums[left]<=target and nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            else:
                # right side is sorted
                if nums[mid]<target and nums[right]>=target:
                    left = mid+1
                else:
                    right = mid-1
        return -1 if nums[left]!=target else left
