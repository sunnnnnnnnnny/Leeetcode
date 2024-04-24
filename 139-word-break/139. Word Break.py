class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # backtracking with checking i is in dict then n-i is?
        # self.wordDictSet = set(wordDict)
        # Will timeout
        def checkStrIsBreakAble(self, sLeft:str):
            if sLeft == "":
                return True
            # print(sLeft)
            for i in range(1,len(sLeft)+1, 1):
                checkIWord = sLeft[:i]
                if checkIWord in self.wordDictSet:
                    if i == len(sLeft):
                        return True
                    if checkStrIsBreakAble(self, sLeft[i:]):
                        return True
            return False
        # return checkStrIsBreakAble(self, s)
        # memo could be replaced by python. cache
        # self.memo = {}
        @cache
        def dp_backtrack(idx):
            if idx<0:
                return True
            # if idx in self.memo:
            #     return self.memo[idx]
            for word in wordDict:
                if s[idx-len(word)+1:idx+1] == word:
                    if dp_backtrack(idx-len(word)):
                        # self.memo[idx] = True
                        return True
            return False
        return dp_backtrack(len(s)-1)

        