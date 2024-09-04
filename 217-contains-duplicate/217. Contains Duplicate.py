class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash table to record exist, then check it -> time:O(n) space:O(n)
        # sort the array and go through it-> time:O(nlogn) space;O(1)
        exist = {}
        for n in nums:
            if n in exist.keys():
                return True
            exist[n] = True
        return False
        