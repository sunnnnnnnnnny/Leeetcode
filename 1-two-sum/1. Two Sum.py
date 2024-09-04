class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort the array then use 2 pointers, time:O(nlogn+n), space:O(1)
        # map to record the visted num, then everytime check if the remain is in the list
        # creating map O(n), check map O(1), time: O(N), space: O(n)
        appeared = {}
        for i in range(len(nums)):
            left = target-nums[i]
            if left in appeared.keys():
                return [i, appeared[left]]
            appeared[nums[i]] = i
        return []