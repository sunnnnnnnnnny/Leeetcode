class MedianFinder:
# by separating the num into 2 data structs
# large num in minHeap, small num in maxHeap, with both size same or small=large+1
# everytime a new number comes in, we know which it shold be 
# time:O(2*logN) for add O(1) for find mied
# space:O(N)
    def __init__(self):
        self.smallSize = 0
        self.maxHeapSmall = []
        self.largeSize = 0
        self.minHeapLar = []

    def addNum(self, num: int) -> None:
        
        if self.smallSize >0 and -self.maxHeapSmall[0]>num:
            heapq.heappush(self.maxHeapSmall, -num)
        elif self.largeSize >0 and self.minHeapLar[0]<=num:
            heapq.heappush(self.minHeapLar, num)
        else:
            heapq.heappush(self.minHeapLar, num)
        
        if len(self.maxHeapSmall) > len(self.minHeapLar):
            toLarge = heapq.heappop(self.maxHeapSmall)
            heapq.heappush(self.minHeapLar, -toLarge)
        elif len(self.maxHeapSmall) < len(self.minHeapLar)-1:
            toSmall = heapq.heappop(self.minHeapLar)
            heapq.heappush(self.maxHeapSmall, -toSmall)
        self.smallSize = len(self.maxHeapSmall)
        self.largeSize = len(self.minHeapLar)
    def findMedian(self) -> float:
        med = 0
        if self.smallSize == self.largeSize:
            med = (-self.maxHeapSmall[0]+self.minHeapLar[0])/2
        else:
            med = self.minHeapLar[0]
        return med
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()