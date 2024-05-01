class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort by ending, then record each meeting room's starting time
        # traverse all interval by try to fit in existing room
        # time: O(nlong+n) = O(nlogn)
        # Space: O(N+N) = sort+traversal to record room time
        room = []
        intervals.sort(key=lambda x:x[0])
        for start, end in intervals:
            roomIdx = -1
            # print('start:', start, end)
            for i in range(len(room)):
                if room[i]<=start:
                    roomIdx = i
                    break
            if roomIdx>=0:
                room[roomIdx] = end
            else:
                room.append(end)
            # print(room)
        return len(room)


        