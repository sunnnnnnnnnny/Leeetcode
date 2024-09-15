class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep the temp into stack, once we are on the new temp
        # pops out the lower temp ones, then we get the diff of (i-preI)
        # time:O(N) space:O(N) to keep record of the previous temp
        preTemp = []
        # store the temp, idx
        ret = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            nowT = temperatures[i]
            while len(preTemp)>0:
                if preTemp[-1][0]<nowT:
                    preT, preIdx = preTemp.pop(-1)
                    dayDiff = i-preIdx
                    ret[preIdx] = dayDiff
                else:
                    break
            preTemp.append([nowT,i])
        return ret