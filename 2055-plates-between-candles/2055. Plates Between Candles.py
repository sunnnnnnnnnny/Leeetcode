class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # to get the left closest candle for the end
        # and get the right closest candle for the start
        # with the precalculated sum of plates til the index(cause inclusive)
        # we can get the sum in between
        # time: O(N*3) = O(N) space:O(N*3)= O(N)
        N = len(s)
        left = [-1]*N
        right = [-1]*N
        preSum = [0]*N
        curSum = 0
        leftIdx, rightIdx = -1, -1
        for i in range(N):
            if s[i] == '|':
                leftIdx = i
            else:
                curSum += 1
            left[i] = leftIdx
            preSum[i] = curSum
        for i in range(N-1, -1, -1):
            if s[i] == '|':
                rightIdx = i
            right[i] = rightIdx
        ret = []
        for query in queries:
            start = query[0]
            end = query[1]
            startPlate = right[start]
            endPlate = left[end]
            btwCandles = 0
            if startPlate>=0 and endPlate>=0 and startPlate<endPlate:
                btwCandles = preSum[endPlate]-preSum[startPlate]
            ret.append(btwCandles)

        return ret

        # brute force: time:O(NM) N is the size of str, M is the size of list
        # keep the record of left and right candle location for each pos
        # then easy to calculate, time: O(N+M) spze:O(N+M)
        # N = len(s)
        # nearestLeft = [0]*N
        # nearestRight = [0]*N
        # candleBtwCnt = [0]*N
        # nearestCandleLeft = -1
        # candleCnt = 0
        # for i in range(N):
        #     if s[i] == '|':
        #         nearestCandleLeft = i
        #         candleCnt += 1
        #     nearestLeft[i] = nearestCandleLeft
        #     candleBtwCnt[i] = candleCnt
        
        # nearestCandleRight = -1
        # for i in range(N-1, -1, -1):
        #     if s[i] == '|':
        #         nearestCandleRight = i
        #     nearestRight[i] = nearestCandleRight
        # ret= []
        # for a,b in queries:
        #     left = nearestRight[a]
        #     right = nearestLeft[b]
        #     if left<0 or right<0:
        #         ret.append(0)
        #         continue
        #     ret.append((right-left+1)-(candleBtwCnt[right]-candleBtwCnt[left]+1) if right>left else 0)
        # return ret

        # binary search one with going over:
        # time: O(N+Mlog(N)) spzce:O(N+M)
        # candleLoc = [i for i,c in enumerate(s) if c == '|']
        # res = []
        # for a,b in queries:
        #     left = bisect.bisect_left(candleLoc, a)
        #     # find the rightmost idx of the num for insert, thus need to minus 1 for actual pos
        #     right = bisect.bisect(candleLoc, b)-1
        #     # get the overall diff of ori array minus the num of candles
        #     res.append((candleLoc[right]-candleLoc[left])-(right-left) if left<right else 0)
        # return res
        