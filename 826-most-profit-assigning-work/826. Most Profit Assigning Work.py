class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # since every worker can complete only one job which we want greedy
        # greedly select the most profitable job each worker can complete
        # sort the jobs by difficulty, and traverse each worker
        # 2. pre calculate the max profit for each diffeculty
        # time:O(NlogN+MN) space:O(N)
        # 3. sort the job by difficulty and the worker by strength increasing
        # then go through with 2 pointer of checking difficulty and strength
        # time:O(nLogn+mlogm+n+m) space:O(n)
        jobs = [(difficulty[i], profit[i]) for i in range(len(profit))]
        jobs.sort(key = lambda x:x[0])
        worker.sort()
        jobIdx = 0
        nowMax = 0
        ret = 0
        for i in range(len(worker)):
            while jobIdx<len(jobs) and worker[i]>=jobs[jobIdx][0]:
                nowMax = max(nowMax, jobs[jobIdx][1])
                jobIdx+=1
            ret+=nowMax
        return ret
        # ret = 0
        # def findMaxProfitOfWorker(strength):
        #     nonlocal difficulty, profit
        #     makeN = 0
        #     for i in range(len(profit)):
        #         if difficulty[i]<=strength:
        #             makeN = max(makeN, profit[i])
        #     return makeN
        # strength2Profit = {}
        # for w in worker:
        #     if w not in strength2Profit.keys():
        #         make = findMaxProfitOfWorker(w)
        #         strength2Profit[w] = make
        #     ret += strength2Profit[w]
        # return ret