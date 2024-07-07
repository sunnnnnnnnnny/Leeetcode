class Solution:
    def checkValidString(self, s: str) -> bool:
        # record * separate, use when unmatched appeared
        # using 2 stacks for open and star idx, 
        # when end using them to balance it open>star
        # only open and star left, try balancing them by openLoc < starLoc
        # time: O(N) space:O(2N) => greedy
        openIdx = []
        starIdx = []
        for i in range(len(s)):
            if s[i] == "(":
                openIdx.append(i)
            elif s[i] == "*":
                starIdx.append(i)
            else:
                if openIdx:
                    openIdx.pop()
                else:
                    if starIdx:
                        starIdx.pop()
                    else:
                        return False
        while openIdx:
            nowOpen = openIdx[-1]
            if starIdx:
                while starIdx:
                    lastStarIdx = starIdx.pop()
                    if lastStarIdx>nowOpen:
                        openIdx.pop()
                        break
            else:
                return False
        return True
        # backtracking dp[i][j] as if s[i:j] is working
        # dp[i][j] == any(dp[i+1]dp[j-1], dp[i+2][j], dp[i][j-2])
        # time: O(n*n) space:O(n*n)
        # dp = [[0 for i in range(len(s))] for j in range(len(s))]
        # def bk(start, end):
        #     if start > end:
        #         return 1
        #     if start == end:
        #         if s[start] == "*":
        #             dp[start][end] = 1
        #         else:
        #             dp[start][end] = -1
        #         return dp[start][end]
        #     if dp[start][end] != 0:
        #         return dp[start][end]
        #     # the right and left
        #     ret = -1
        #     if s[start] == "*":
        #         if s[end] == ")":
        #             if bk(start+1, end-1)==1:
        #                 ret = 1
        #         if bk(start+1, end)==1:
        #                 ret = 1
            
        #     if s[start] == "(":
        #         if s[end] == ")" or s[end] == "*":
        #             if bk(start+1, end-1)==1:
        #                 ret = 1
        #         if s[end] == "*":
        #             if bk(start, end-1)==1:
        #                     ret = 1
        #     dp[start][end] = ret
        #     return ret
        # ans = bk(0,len(s)-1)
        # return ans
            


            




        


        