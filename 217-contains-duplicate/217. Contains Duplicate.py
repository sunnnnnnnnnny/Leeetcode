class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashmap to record the number appeared
        # return true when there's same num appeared
        # time: O(N) traverse the nums and look up in hash O(1)
        # space: O(N) for hashmap
        hashMap = {}
        for num in nums:
            if num in hashMap.keys():
                return True
            hashMap[num] = 1
        return False
        