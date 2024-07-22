class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # time: O(nLogN+N) space:O(N) for recording the heighttoIdx
        height2Idx = [(heights[i], i) for i in range(len(heights))]
        height2Idx.sort(reverse = True)
        # print(height2Idx)
        ret = []
        for i in range(len(height2Idx)):
            h, i = height2Idx[i]
            ret.append(names[i])
        return ret
        