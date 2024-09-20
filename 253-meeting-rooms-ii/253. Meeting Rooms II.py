class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the room with end time of increasing 
        # using the minHeap for end time, if the next end>minHeap head
        # then we need one more room, 
        # time:O(NlogN+NlogK) K is the size of room
        # space:O(N)
        intervals.sort(key = lambda x:x[0])
        meetEnd = []
        for meet in intervals:
            iEnd = meet[1]
            if len(meetEnd)>0 and meetEnd[0]<=meet[0]:
                heapq.heappop(meetEnd)
            heapq.heappush(meetEnd, iEnd)
        return len(meetEnd)