class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the time from start?
        # record the occupied meeting room end time, with minHead
        # use the first released meeting room
        # time;O(NlogN+N) space:O(N)
        room = []
        intervals.sort(key= lambda x:x[0])
        for meet in intervals:
            s, e = meet
            if len(room) == 0:
                heapq.heappush(room, e)
                continue
            topMeet = room[0]
            if topMeet <= s:
                heapq.heappop(room)
            heapq.heappush(room, e)
        return len(room)