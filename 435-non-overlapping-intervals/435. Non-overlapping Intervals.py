class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the interval by end increasing
        # b/c the earlier it ends, we can take more intecval
        # greedy taking the possible interval, and remove any overlapped one
        # time:O(NlogN+N) space:O(N)
        intervals.sort(key=lambda x:x[1])
        prevEnd = intervals[0][1]
        removeCnt = 0
        # print(intervals)
        for i in range(1,len(intervals)):
            if intervals[i][0]<prevEnd:
                # overlapp
                removeCnt+=1
            else:
                prevEnd = intervals[i][1]
        return removeCnt
