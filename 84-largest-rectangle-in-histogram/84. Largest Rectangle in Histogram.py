class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # similar to trapping rain? 
        # using the stack to get the increasing heights, thus the area would be
        # the last in stack *width
        # time:O(N) space:O(N)
        inS = []
        ret = 0
        for i in range(len(heights)):
            if len(inS) >0:
                while inS:
                    preI, prevS = inS[-1]
                    if heights[i]<prevS:
                        inS.pop()
                        ppI = -1
                        if len(inS)>0:
                            ppI, ppS = inS[-1]
                        now = prevS*(i-ppI-1)
                        ret = max(ret, now)
                    else:
                        break
            inS.append([i, heights[i]])
        end = len(heights)
        while inS:
            preI, prevS = inS.pop()
            ppI = -1
            if len(inS)>0:
                ppI, ppS = inS[-1]
            now = prevS*(end-ppI-1)
            ret = max(ret, now)
        return ret     
        # by taking it's self as the min height, see how far the width go
        # time:O(N*N) space:O(1)
        # TLE
        # ret = 0
        # for i in range(0, len(heights)):
        #     h = heights[i]
        #     for j in range(i, len(heights)):
        #         h = min(h,heights[j])
        #         width = j-i+1
        #         now = h*width
        #         ret = max(ret, now)
        # return ret
