class TimeMap:
# if the timestamp is not strick increasing, 
# then we need to use binary search to find the insert position
# method 1: keep the key as key with sorted by timestamp to val
# method 2: keep the timestamp as key, and keep the item as key to val
# time:O(logN+N)  space:O(N)
    def __init__(self):
        self.key2TimeVal = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key2TimeVal:
            self.key2TimeVal[key] = []
        self.key2TimeVal[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key2TimeVal:
            return ""
        if timestamp<self.key2TimeVal[key][0][0]:
            return ""
        idx = bisect.bisect_left(self.key2TimeVal[key], timestamp, key=lambda x: x[0])
        # print(self.key2TimeVal[key], idx, timestamp)
        if idx>=len(self.key2TimeVal[key]):
            idx = len(self.key2TimeVal[key])-1
        if self.key2TimeVal[key][idx][0]>timestamp:
            idx-=1
        return self.key2TimeVal[key][idx][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)