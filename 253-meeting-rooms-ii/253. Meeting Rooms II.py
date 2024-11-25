class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # using minHeap to record the current in use meeting room end time
        # always use the meeting room with first end time
        # time:O(NlogN) space:O(N)
        # sort the meetings with start time
        intervals.sort(key = lambda x:x[0])
        meetR = []
        for meet in intervals:
            s, e = meet
            if meetR and meetR[0]<=s:
                heapq.heappop(meetR)
            heapq.heappush(meetR, e)
        return len(meetR)