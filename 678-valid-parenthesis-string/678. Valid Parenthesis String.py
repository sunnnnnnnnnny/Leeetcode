class Solution:
    def checkValidString(self, s: str) -> bool:
        # record * separate, use when unmatched appeared
        # using 2 stacks for open and star idx, 
        # when end using them to balance it open>star
        # only open and star left, try balancing them by openLoc < starLoc
        # time: O(N) space:O(2N) => greedy
        # openIdx = []
        # starIdx = []
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         openIdx.append(i)
        #     elif s[i] == "*":
        #         starIdx.append(i)
        #     else:
        #         if openIdx:
        #             openIdx.pop()
        #         else:
        #             if starIdx:
        #                 starIdx.pop()
        #             else:
        #                 return False
        # while openIdx:
        #     nowOpen = openIdx[-1]
        #     if starIdx:
        #         while starIdx:
        #             lastStarIdx = starIdx.pop()
        #             if lastStarIdx>nowOpen:
        #                 openIdx.pop()
        #                 break
        #     else:
        #         return False
        # return True
        # backtracking dp[i][j] represents 
        # if the substring starting from index i is valid with j opening brackets
        # dp[i][j] == any(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
        # time: O(n*n) space:O(n*n)
        n = len(s)
        dp = [[-1] *(n) for _ in range(n)]
        def bk(idx, openCnt):
            if idx == len(s):
                return openCnt == 0
            if dp[idx][openCnt]!=-1:
                return dp[idx][openCnt] == -1
            isValid = False
            if s[idx] == "*":
                # treat as open
                isValid |= bk(idx+1, openCnt+1)
                if openCnt>0:
                    # treat as close
                    isValid |= bk(idx+1, openCnt-1)
                isValid |= bk(idx+1, openCnt)
            else:
                if s[idx] == "(":
                    isValid |= bk(idx+1, openCnt+1)
                elif openCnt>0:
                    isValid |= bk(idx+1, openCnt-1)
            dp[idx][openCnt] = 1 if isValid else 0
            return isValid
        
        return bk(0, 0)



            




        


        