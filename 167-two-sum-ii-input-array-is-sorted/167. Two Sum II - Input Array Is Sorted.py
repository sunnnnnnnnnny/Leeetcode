class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # as the array is sorted of non-decreasing order
        # by 2 pointers we can try to find the numbers 
        # from both end
        # while we need larger nums then we move the left
        # with less num then move right
        # time: O(N) space:O(1)
        left = 0
        right = len(numbers)-1
        while left<right:
            curSum = numbers[left]+numbers[right]
            if curSum == target:
                return [left+1, right+1]
            elif curSum>target:
                right -= 1
            elif curSum<target:
                left += 1
        return [left+1, right+1]
        