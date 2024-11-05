class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # always select the left freq number in the backtracking, for avoiding the duplicate
        counts = collections.Counter(nums)
        ret = []
        def backtrack(nowPer, n, counter):
            nonlocal nums, ret
            if len(nowPer) == n:
                ret.append(list(nowPer))
                return
            for k in counter:
                if counter[k]>0:
                    nowPer.append(k)
                    counter[k] -= 1
                    backtrack(nowPer, n, counter)
                    nowPer.pop()
                    counter[k] += 1
            return
        n = len(nums)
        backtrack([], n, counts)
        return ret