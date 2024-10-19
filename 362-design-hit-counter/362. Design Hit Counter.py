class HitCounter:
# since the timestamp is monotonically increasing, we could use a queue 
# to record the past 300 second up items
# time:O(N) for each check of the past 300 getHits
# space:O(N)
    def __init__(self):
        self.pastHit = []

    def hit(self, timestamp: int) -> None:
        self.pastHit.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        beginT = timestamp-300
        while self.pastHit:
            firstT = self.pastHit[0]
            if firstT<=beginT:
                self.pastHit.pop(0)
            else:
                break
        return len(self.pastHit)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)