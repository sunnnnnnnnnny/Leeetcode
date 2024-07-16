class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # get the highest building height from the right
        # keep such record and add the index of building
        # if the building height>highest height of right
        # assume all height is positive
        # time:O(N) space:O(1)
        hightestR = 0
        ret = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i]>hightestR:
                # ret = [i]+ret
                ret.append(i)
            hightestR = max(hightestR, heights[i])
        return ret[::-1]