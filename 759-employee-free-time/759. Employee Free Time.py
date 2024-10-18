"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # merge all the employ work time, then going through it 
        # first sort the time in flattened as start time
        # the breaks will be it's overlapped free time
        # time:O(N*M), space:O(M)
        emptyTime = []
        busyTime = []
        for j in range(len(schedule)):
            for i in range(len(schedule[j])):
                busyTime.append([schedule[j][i].start, schedule[j][i].end])
        # print(busyTime)
        busyTime.sort(key = lambda x:(x[0], x[1]))
        # print(busyTime)
        mBusy = [[busyTime[0][0], busyTime[0][1]]]
        # print(mBusy)
        for i in range(1, len(busyTime)):
            preS, preE = mBusy[-1]
            nowS, nowE = busyTime[i]
            # print(i, preS, preE, nowS, nowE)
            if nowS>=preS and nowS<=preE:
                mBusy[-1][1] = max(preE, nowE)
            else:
                empInt = Interval(preE, nowS)
                emptyTime.append(empInt)
                mBusy.append([nowS, nowE])
        # print(emptyTime)
        return emptyTime



        # for j in range(len(schedule)):
        #     for i in range(len(schedule[j])):
        #         busyTime.append([schedule[j][i].start, schedule[j][i].end])
        # # print(busyTime)
        # busyTime.sort(key = lambda x:(x[0], x[1]))
        # # print(busyTime)
        # mBusy = [[busyTime[0][0], busyTime[0][1]]]
        # # print(mBusy)
        # for i in range(1, len(busyTime)):
        #     preS, preE = mBusy[-1]
        #     nowS, nowE = busyTime[i]
        #     # print(i, preS, preE, nowS, nowE)
        #     if nowS>=preS and nowS<=preE:
        #         mBusy[-1][1] = max(preE, nowE)
        #     else:
        #         emptyTime.append([preE, nowS])
        #         mBusy.append([nowS, nowE])
        # print(emptyTime)
        # return emptyTime

        