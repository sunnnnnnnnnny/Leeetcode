class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # record the current finish time and compare with arrive time
        # to calculate the waittime: 
        curFinishTime = 0
        totalTimeWait = 0.0
        for cusTime in customers:
            arrive = cusTime[0]
            need = cusTime[1]
            if curFinishTime<arrive:
                curFinishTime = arrive+need
                totalTimeWait += need
            else:
                curFinishTime += need
                totalTimeWait += (curFinishTime-arrive)
        return totalTimeWait/len(customers)
        