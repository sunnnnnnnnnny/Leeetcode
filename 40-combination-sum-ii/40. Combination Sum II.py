class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the numbers, X using pointers 
        # time:O(nlogn+target*n) space:O(n)
        candidates.sort()
        ret = []
        self.backTracking(candidates, target, 0, [], ret)
        return ret
        # dp? building the unique combination would cause O(target*n)
        # time: O(2^n) space:O(n)
    def backTracking(self, candidates, newTarget, totalIdx, path, ret):
        if newTarget<0:
            return
        if newTarget == 0:
            ret.append(path)
            return
        for i in range(totalIdx, len(candidates)):
            # for each round we would only have the same number selected once
            # could prevent the duplication
            if i>totalIdx and candidates[i] == candidates[i-1]:
                continue
            self.backTracking(candidates, newTarget-candidates[i], i+1, path+[candidates[i]], ret)


        