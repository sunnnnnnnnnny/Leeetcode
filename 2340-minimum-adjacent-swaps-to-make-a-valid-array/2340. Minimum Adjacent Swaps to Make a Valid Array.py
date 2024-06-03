class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        # get the rightmost max to do the swap
        # and get the leftmost min to do the swap
        # time: O(N) space:O(1)
        minNum = min(nums)
        idxLeft = nums.index(minNum)
        nums = [nums[idxLeft]] + nums[:idxLeft] + nums[idxLeft+1:]

        maxNum = max(nums)
        # getting the right most max
        idxRight = nums[::-1].index(maxNum)
        return idxLeft+idxRight