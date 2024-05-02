class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 1. sort+traverse with min heap
        # sort by ending, then record each meeting room's starting time
        # using min heap to keep record of the earliest possible released room
        # assgin that empty room to the new meeting
        # (wrong)traverse all interval by try to fit in existing room
        # time: O(nlong+n) = O(nlogn)
        # Space: O(N+N) = sort+traversal to record room time
        room = []
        intervals.sort(key=lambda x:x[0])
        # take the first meeting directly
        room.append(intervals[0][1])
        heapq.heapify(room)
 
        for start, end in intervals[1:]:
            roomIdx = -1
            # print('start:', start, end)
            if room[0]<=start:
                heapq.heappop(room)
            heapq.heappush(room, end)
            # print(room)
        return len(room)


        