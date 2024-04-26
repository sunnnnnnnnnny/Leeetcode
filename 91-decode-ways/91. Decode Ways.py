class Solution:
    def numDecodings(self, s: str) -> int:
        # each char can be group single or in two
        # dp[i] = (if s[i-1:1] is valid)dp[i-1]+(if s[i-1:2] is valid)dp[i-2]
        def isValidLetter(subS:str)->bool:
            if len(subS)<1 or subS[0] == '0':
                return False
            # print(subS)
            inDigit = int(subS)
            if inDigit>0 and inDigit<27:
                return True
            return False
        dpList = [0]*len(s)
        dpList[0] = 1 if isValidLetter(s[0:1]) else 0
        if dpList[0] == 0 or len(s)==1:
            return dpList[0]
        
        # python substr is start:end
        dpList[1] = dpList[0] if isValidLetter(s[1:2]) else 0
        dpList[1] += 1 if isValidLetter(s[0:2]) else 0
        for i in range(2, len(s), 1):
            dpList[i] += dpList[i-1] if isValidLetter(s[i:i+1]) else 0
            dpList[i] += dpList[i-2] if isValidLetter(s[i-1:i+1]) else 0
            # print('i: ',i, dpList)
        return dpList[len(s)-1]

        