class HitCounter:
# since we only need to check the past 5 min = 300 sec of the record
# we use hashMap for record the hit at each sec
# getHits will go through the past 300 sec to accumulate the hit
# time:O(1) for hit, getHit will be O(300) = O(1)
# space:O(N) depending on the unique timestampes
# method 2 by using queue FIFO for the timestamp
# since it's chronological, we can get the past 300 sec record in queue
# record the hits, time:O(300) = O(1) for any of it
    def __init__(self):
        self.timeHitCnt = {}
        self.timeHitCache = {}

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.timeHitCnt.keys():
            self.timeHitCnt[timestamp] = 0
        self.timeHitCnt[timestamp]+=1

    def getHits(self, timestamp: int) -> int:
        ret = 0
        for i in range(timestamp, timestamp-300, -1):
            if i in self.timeHitCnt.keys():
                ret += self.timeHitCnt[i]
        return ret


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)