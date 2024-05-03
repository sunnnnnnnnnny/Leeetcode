class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # get all the start time and end time
        # use binary search to get the insertion where the location of newInterval
        if len(newInterval) != 2:
            return intervals
        if len(intervals) == 0:
            return [newInterval]
        insertStart = newInterval[0]
        insertEnd = newInterval[1]
        def binarySearch(start):
            # if intervals[0][0]>=start:
            #     return 0
            # if intervals[-1][1]<=start:
            #     return len(intervals)-1
            highIdx = len(intervals)-1
            lowIdx = 0
            while highIdx>=lowIdx:
                mid = int(lowIdx+(highIdx-lowIdx)/2)
                if intervals[mid][0]<start:
                    lowIdx = mid+1
                else:
                    highIdx = mid-1
            return lowIdx
        insertIdx = binarySearch(insertStart)
        # only getting where this interval should be inserted
        # still need to traverse the whole interval for checking none overlapped
        print(insertIdx)
        intervals.insert(insertIdx, newInterval)
        ret = []
        # python sublist is start<=x<end, doesn't include end
        # start merging the possible intervals
        for interval in intervals:
            if not ret or ret[-1][1]<interval[0]:
                ret.append(interval)
            # since the start is sorted ascending order, 
            # it's garuentee that start is the smaller num
            else:
                ret[-1][1] = max(ret[-1][1], interval[1])

        # ret = []
        # idx = 0
        # n = len(intervals)
        # # add the interval not overlap with new one
        # while idx < n and intervals[idx][1]<insertStart:
        #     ret.append(intervals[idx])
        #     idx += 1

        # while idx < n and intervals[idx][0]<=insertEnd:
        #     insertStart = min(insertStart, intervals[idx][0])
        #     insertEnd = max(insertEnd, intervals[idx][1])
        #     idx += 1
        # ret.append([insertStart, insertEnd])

        # while idx < n:
        #     ret.append(intervals[idx])
        #     idx += 1
        return ret
        
