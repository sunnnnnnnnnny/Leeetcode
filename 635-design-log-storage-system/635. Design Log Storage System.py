class LogSystem:
# store the timestamp as increasing order, then every time we retrieve it, do a binary search on it based on the granularity
# time:O(logN+N) for put time:O(logN+N) for retrieve space:O(N)
    def __init__(self):
        self.logs = []
        self.ignore = ["Year","Month","Day","Hour","Minute","Second"]
        # self.uniId = set()

    def convertTs(self, timestamp:str)->int:
        ti = timestamp.split(':')
        y, m, d, h, mins, secs = ti
        # print(timestamp, ti)
        intTi = 0
        for i in range(len(ti)):
            intTi *= 100
            intTi += int(ti[i])
        return intTi
    def put(self, id: int, timestamp: str) -> None:
        # if id in self.uniId:
        #     return
        intTi = self.convertTs(timestamp)
        # Sort by the second element (quantity)
        def getTs(item):
            return item[0]
        insertIdx = bisect.bisect_left(self.logs, intTi, key = getTs)
        self.logs.insert(insertIdx, [intTi, id, timestamp])
        # print(timestamp, insertIdx, self.logs)
        # self.uniId.add(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        intTiStart = self.convertTs(start)
        intTiEnd = self.convertTs(end)
        grand = 1
        for i in range(len(self.ignore)-1, -1, -1):
            if self.ignore[i] == granularity:
                break
            grand *= 100
        # print(granularity, grand)
        intTiStart = (intTiStart//grand)*grand
        intTiEnd = (intTiEnd//grand+1)*grand
        # print(start, intTiStart)
        # print(end, intTiEnd)
        # Sort by the second element (quantity)
        def getTs(item):
            return item[0]
        startI = bisect.bisect_left(self.logs, intTiStart, key = getTs)
        endI = bisect.bisect_left(self.logs, intTiEnd, key = getTs)
        # print(start, end, startI, endI, self.logs)
        ret = []
        for i in range(startI, min(endI, len(self.logs))):
            if i>0 and self.logs[i][0] == self.logs[i-1][0] and self.logs[i][1] == self.logs[i-1][1]:
                continue
            ret.append(self.logs[i][1])
        return ret


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)