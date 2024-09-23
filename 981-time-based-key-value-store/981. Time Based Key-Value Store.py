class TimeMap:

    def __init__(self):
        self.timeKey = []
        self.time2Val = {}
#  time:O(logn+n) space:O(N)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.time2Val.keys():
            self.time2Val[timestamp] = {}
            insertIdx = bisect.bisect_left(self.timeKey, timestamp)
            # print("set ",timestamp, insertIdx)
            self.timeKey.insert(insertIdx, timestamp)
        
        self.time2Val[timestamp][key] = value
# time:O(logn+n)
    def get(self, key: str, timestamp: int) -> str:
        checkIdx = bisect.bisect_left(self.timeKey, timestamp)
        endCheckIdx = checkIdx if checkIdx<len(self.timeKey) else len(self.timeKey)-1
        # print(self.timeKey)
        # print(timestamp, checkIdx, endCheckIdx)
        for i in range(endCheckIdx, -1, -1):
            if self.timeKey[i]<=timestamp and key in self.time2Val[self.timeKey[i]].keys():
                return self.time2Val[self.timeKey[i]][key]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)