class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = dp[i-1](if not 0 and <9)+( if s[i-1:i] is valid )dp[i-2]
        # time:O(N) space:O(N) but can be optimized as O(1)
        N = len(s)
        if N==0:
            return 0
        elif N==1:
            return 0 if ord(s[0])-ord('0')==0 else 1
        dp = [0 for i in range(N+1)]
        dp[0] = dp[1] = 1
        if ord(s[0])-ord('0')==0:
            dp[1] = 0
        print(dp)
        for i in range(1,N):
            if ord(s[i])-ord('0')>0 and ord(s[i])-ord('0')<10:
                dp[i+1]+=dp[i]
            # print(i, s[i-1:i+1], dp)
            if ord(s[i-1])-ord('0')>0 and int(s[i-1:i+1])<=26:
                dp[i+1]+=dp[i-1]
        return dp[-1]