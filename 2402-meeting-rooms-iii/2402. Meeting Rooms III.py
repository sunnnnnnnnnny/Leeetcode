class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort the meeting with start time
        # keep the meeting room end time with order of end, room num
        # using a counter for the meeting room usage
        # time:O(MlogM+M*logN) space:O(N+N)
        mCnt = [0]*n
        meetE = []
        maxRoomIdx = 0
        availableRoom = []
        for i in range(n):
            heapq.heappush(availableRoom, i)
        meetings.sort(key = lambda x:x[0])
        for meet in meetings:
            s, e = meet
            # release the in use meeting room
            while meetE:
                endT, idx =  meetE[0]
                if endT<=s:
                    heapq.heappop(meetE)
                    heapq.heappush(availableRoom, idx)
                else:
                    break
            useRoomIdx = -1
            if availableRoom:
                useRoomIdx = heapq.heappop(availableRoom)
                heapq.heappush(meetE, (e, useRoomIdx))
            else:
                actualEnd, useRoomIdx = heapq.heappop(meetE)
                heapq.heappush(meetE, (actualEnd+(e-s), useRoomIdx))
            mCnt[useRoomIdx] += 1
            if mCnt[useRoomIdx]>=mCnt[maxRoomIdx]:
                maxRoomIdx = useRoomIdx if mCnt[useRoomIdx]>mCnt[maxRoomIdx] else min(useRoomIdx, maxRoomIdx)
        return maxRoomIdx