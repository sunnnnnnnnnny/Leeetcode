class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # dp by selecting the jobs
        # sort the jobs by start time and having the option to take it or not
        # dp[i][0] = not taking the job = previous not conflict profit
        # dp[i][1] = take the job, previous non conflict profit+profit[i]
        # maxProfit = max(dp)
        # time: O(2^N) space:O(2N) memorization
        tasks = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        tasks.sort(key = lambda x:x[0])
        n = len(startTime)
        dp = [[0,0]for i in range(len(startTime))]
        memo = [-1 for i in range(n)]
        # print(tasks)
        def checkProfit(startT, prevI):
            nonlocal dp, tasks, n, memo
            nextStartI = bisect.bisect_left(tasks, (startT, ), prevI)
            # print(startT, nextStartI, prevI)
            if nextStartI>=n:
                return 0
            # memo is /??
            if memo[nextStartI]!= -1:
                return memo[nextStartI]
            takeIt = checkProfit(tasks[nextStartI][1],  nextStartI)+tasks[nextStartI][2]
            notTake = checkProfit(startT, nextStartI+1)
            memo[nextStartI] = max(takeIt, notTake)
            return memo[nextStartI]
        ret =  checkProfit(0, 0)
        # print(dp)
        return ret