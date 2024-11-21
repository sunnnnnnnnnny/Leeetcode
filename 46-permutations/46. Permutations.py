class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def bk(curr):
            if len(curr) == len(nums):
                # need deep copy
                # ret.append(curr[:])
                ret.append(copy.deepcopy(curr))
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    # print(n, curr)
                    bk(curr)
                    curr.pop()

        bk([])
        return ret
