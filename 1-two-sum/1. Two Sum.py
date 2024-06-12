class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # with the intuitive of leftNum is target-num
        # keep record of the appeared num then check if it exists
        # if it does we get the ans
        # time: O(N) traverse list and hash look up
        # space: O(N) for the hashMap
        appeared = {}
        for i in range(len(nums)):
            need = target-nums[i]
            if need in appeared.keys():
                return [i, appeared[need]]
            appeared[nums[i]] = i
        return [-1, -1]

        