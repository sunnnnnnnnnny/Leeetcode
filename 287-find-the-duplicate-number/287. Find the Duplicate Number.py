class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hashSet to record the appeared num
        # time:O(N) space:O(N)
        # since only one repeating num
        # brute force is to get the array len, check each n one by one
        # time:O(N^N) space:O(1)
        # method 2 binary search
        # count the numbers that's smaller than mid
        # time:O(nlogn) space:O(1)
        def countSmaller(nums, now):
            ret = 0
            for n in nums:
                if n<=now:
                    ret+=1
            return ret
        left = 1
        right = len(nums)
        while left<=right:
            mid = (left+right)//2
            if countSmaller(nums, mid)>mid:
                right = mid-1
            else:left = mid+1
        return left
        


        