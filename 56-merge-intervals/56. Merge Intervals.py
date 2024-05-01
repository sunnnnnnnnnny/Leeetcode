class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the start of interval, then traverse each one to merge them
        # time: O(NlogN+N) sorint+traversal
        # space: O(N) at most having all none overlapped interval
        intervals.sort(key = lambda x:x[0])
        merge =[]
        for interval in intervals:
            #  if the merge is empty or the last merge interval end < new start(no overlap)
            if not merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else:
                # start merging
                merge[-1][1] = max(merge[-1][1], interval[1])
        return merge

        