class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using the priority queue to set the cur cycle ones
        # always select the top freq ones
        # putting it back after the cycle
        # time:O(NlogN) space:O(N)
        time = 0
        char2Cnt = collections.Counter(tasks)
        # print(char2Cnt)
        topFreq = []
        for k, freq in char2Cnt.items():
            heapq.heappush(topFreq, (-freq,k))
        while len(topFreq)>0:
            tempReq = []
            usedT = 0
            for i in range(n+1):
                if topFreq:
                    nowUse = heapq.heappop(topFreq)
                    if -nowUse[0]-1 > 0 :
                        tempReq.append((-nowUse[0]-1, nowUse[1]))
                    usedT = i+1
                else:
                    break
            # print(time, tempReq, usedT)
            time = time + usedT if len(tempReq) == 0 else time+n+1
            for it in tempReq:
                heapq.heappush(topFreq, (-it[0],it[1]))
        return time