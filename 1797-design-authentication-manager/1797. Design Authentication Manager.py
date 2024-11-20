class AuthenticationManager:

    def __init__(self, timeToLive: int):
        # usiing dict to record the tokeId with expireTs
        # keep minHeap for timestamp to tokeID for easier count none expire
        # time:O(1) for generate, renew/count O(nlogn)
        # using orderedDict to keep the expT as increasing, so time:O(N)
        self.ttl = timeToLive
        self.toke2Exp = {}
        self.ts2TokeMinHeap = []

    def generate(self, tokenId: str, currentTime: int) -> None:
        expT = currentTime+self.ttl
        self.toke2Exp[tokenId] = expT
        heapq.heappush(self.ts2TokeMinHeap, [expT, tokenId])
    def clearExp(self, currentTime)->None:
        while self.ts2TokeMinHeap:
            if self.ts2TokeMinHeap[0][0]<=currentTime:
                expTime, expToken = heapq.heappop(self.ts2TokeMinHeap)
                if expToken in self.toke2Exp and self.toke2Exp[expToken]==expTime:
                    del self.toke2Exp[expToken]
            else:
                break
    def renew(self, tokenId: str, currentTime: int) -> None:
        expT = currentTime+self.ttl
        self.clearExp(currentTime)
        if tokenId in self.toke2Exp:
            self.toke2Exp[tokenId] = expT
            heapq.heappush(self.ts2TokeMinHeap, [expT, tokenId])

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.clearExp(currentTime)
        return len(self.toke2Exp)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)