class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the array by start time then check if overlappes
        # time: O(nlogn+n) no extra space
        # need to check what's the definition of overlap
        # brute force, add all time slot as key, then check if exists :time:O(M) too long
        intervals.sort(key = lambda x:x[0])
        prev = []
        for i in range(1, len(intervals)):
            nowS, nowT = intervals[i]
            if nowS>=intervals[i-1][0] and nowS<intervals[i-1][1]:
                return False
        return True
