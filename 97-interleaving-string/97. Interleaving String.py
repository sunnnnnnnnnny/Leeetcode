class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] = s1 i and s2 j can form up the of s3 at some points
        # don't know where the n and m is used
        # time: O(N*M) of len(s1)*Len(s2)
        # space: O(N*M)
        def canInterLeave(i, j, k):
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j==len(s2):
                return s1[i:] == s3[k:]
            if dp[i][j]>=0:
                return dp[i][j] == 1
            ans = False
            if (
                s3[k] == s1[i] and canInterLeave(i+1, j, k+1)
                or
                s3[k] == s2[j]and canInterLeave(i, j+1, k+1)
            ):
               ans = True
            dp[i][j] = 1 if ans else 0
            return ans
        if len(s1)+len(s2)!=len(s3):
            return False
        dp = [[-1 for i in range(len(s2))] for j in range(len(s1)) ]
        return canInterLeave(0, 0, 0)


        