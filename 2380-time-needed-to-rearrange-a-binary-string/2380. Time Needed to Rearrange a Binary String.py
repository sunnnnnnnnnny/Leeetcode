class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # DP use the 1 and 0 in front of it => O(N)
        # b/c the zero will be flipped to later places
        zeros = 0
        sec = 0
        for i in range(len(s)):
            if s[i] == '1':
                if zeros>0:
                    sec = max(sec+1, zeros)
            else:
                zeros += 1
        return sec

        # simulate the process, will take a long time O(N^2)
        # ls = [s[i] for i in range(len(s))]
        # def findZO(listIn, n):
        #     for i in range(1, n):
        #         if listIn[i]=='1' and listIn[i-1]=='0':
        #             return True
        #     return False
        # n = len(s)
        # cnt = 0
        # while findZO(ls, n):
        #     newLs = ls[:]
        #     cnt += 1
        #     for i in range(1, n):
        #         if ls[i]=='1' and ls[i-1]=='0':
        #             newLs[i]='0'
        #             newLs[i-1]='1'
        #     ls = newLs
        # return cnt
