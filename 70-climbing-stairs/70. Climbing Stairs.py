class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        # dp being the n-1 + n-2 as both can reach stair n
        dpList = list()
        # at step 0 is 1 while step 1 is 1
        dpList.append(1)
        dpList.append(1)
        for i in range(2, n+1, 1):
            dpList.append(dpList[i-1]+dpList[i-2])
        return dpList[n]
        


        