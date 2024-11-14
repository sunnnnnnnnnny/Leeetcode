class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort the job in start order, then using backtracking to go through the jobs
        # time:O(nlogn) space:O(n)
        # sort takes O(nlogn) with we check each idx of 2 times with finding the next position by O(logn), also memo call takes O(1)
        # time: O(nlogn + 2n*(logn+1)) = O(nlogn+2nlogn+2n) = O(nlogn)
        # dp[i][0] = max(not considering i job) with dp[i][1] = max( profitI+nonOverlapped)
        jobs = []
        n = len(profit)
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key = lambda x:(x[0], x[1]))

        # with sorting + priority queue, we can use minHeap to append the current to only the top possible elements
        # while only pushing back the max appended element, then lastly pop out all the pq to get the max so far
        # time:O(nlogn+nlogn) space:O(n)
        pq = []
        maxRet = 0
        for i in range(n):
            s, e, p = jobs[i]
            # print(i, pq)
            while pq and pq[0][0]<=s:
                prevEnd, prevProfit = heapq.heappop(pq)
                # the current maxRet would be anything that finished before this s starts
                maxRet = max(maxRet, prevProfit)
            # thus pushing the max+p so far can be that max until using job[i]'s max profit
            heapq.heappush(pq, [e, maxRet+p])
        while pq:
            prevEnd, prevProfit = heapq.heappop(pq)
            maxRet = max(prevProfit, maxRet)
        return maxRet
        # startK = [x[0] for x in jobs]
        # ret = 0
        # memo = {}
        # def bk(idx, prevEnd):
        #     nonlocal n ,ret, memo, jobs, startK
        #     if idx >= n:
        #         return 0
        #     if idx in memo:
        #         return memo[idx]
        #     nextIdx = bisect.bisect_left(startK,jobs[idx][1])
        #     # print(idx, jobs[idx][1], nextIdx)
        #     maxNow = max(bk(nextIdx, jobs[idx][1])+jobs[idx][2], bk(idx+1, prevEnd))
        #     memo[idx] = maxNow
        #     return maxNow
        # ret = bk(0, 0)
        # return ret