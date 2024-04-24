class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # the possible combine is (target-coins)
        # how to dedup(X),if target is 3 coin[1,2], then sum of [1]&[2] is 2 
        self.combine = {}
        self.combine[0] = 1
        def dp_bk(self, checkNum):
            # should I consider negative num
            if checkNum in self.combine:
                return self.combine[checkNum]
            combineCnt = 0
            # print('checkNum? nums?',checkNum, len(nums))
            for num in nums:
                if num>checkNum:
                    continue
                combineCnt += dp_bk(self, checkNum-num)
            self.combine[checkNum] = combineCnt
            return combineCnt
        dp_bk(self, target)
        return self.combine[target]

