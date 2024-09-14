class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] meaning if string[:i] is a valid word break
        # dp[i] = true if dp[true] and s[j+1:i+1] is a word where j<i
        # time:O(n^n) space:O(N)
        # backtracking
        n = len(s)
        memo = [0 for i in range(n)]
        validWord = set()
        for word in wordDict:
            validWord.add(word)
        def checkWord(idx):
            nonlocal memo, validWord,s
            if idx == -1:
                return 1
            if memo[idx]!=0:
                return memo[idx]
            ret = -1
            for i in range(idx,-1,-1):
                if s[i:idx+1] in validWord:
                    if checkWord(i-1)==1:
                        ret = 1
                        break
            memo[idx] = ret
            return memo[idx]
        rest = checkWord(n-1)
        # print(memo)
        return rest==1
         