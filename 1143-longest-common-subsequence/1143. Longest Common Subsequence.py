class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # since dp[i][j] = lcs of str1[0:i] & str2[0:j]
        # dp[i][j] = dp[i-1][j-1]+1 if str1[i] == str2[j]
        # else max(dp[i-1][j], dp[i][j-1])
        # time: O(M*N)
        # memo = [[-1]*len(text2)]*len(text1)
        m = len(text1)
        n = len(text2)
        memo = [[-1 for i in range(n)] for j in range(m)]
        # memo[0][0] = 1 if text1[0] == text2[0] else 0
        # print(memo)
        def lcs(self, str1, str2, i, j, memo):
            if i<0 or j<0:
                return 0
            # NOTE: python will allow neg idx, thus this always block the correct computation
            if memo[i][j] >= 0:
                return memo[i][j]
            # print('i: j:, str:', i, j, str1[i], str2[j])
            if str1[i] == str2[j]:
                memo[i][j] = 1+lcs(self, str1, str2, i-1, j-1, memo)
            else:
                memo[i][j] = max(lcs(self, str1, str2, i-1, j, memo), lcs(self, str1, str2, i, j-1, memo))
            
            return memo[i][j]
        
        ret =  lcs(self, text1, text2, len(text1)-1, len(text2)-1, memo)
        # print(memo)
        return ret