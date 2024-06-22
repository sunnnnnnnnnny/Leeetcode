class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # backtracking
        # time: O(N^3)
        memo = {}
        for word in wordDict:
            memo[word] = True
        def backTrack(leftS:str):
            if len(leftS) == 0:
                return True
            if leftS in memo.keys():
                return memo[leftS]
            ans = False
            for i in range(len(leftS)-1, -1, -1):
                if leftS[i:] in memo.keys() and memo[leftS[i:]] == True:
                    ret = backTrack(leftS[:i])
                    if ret == True:
                        ans = True
                        break
            memo[leftS] = ans
            return ans
        ans = backTrack(s)
        return ans

        # backtracking with checking i is in dict then n-i is?
        # self.wordDictSet = set(wordDict)
        # Will timeout
        # def checkStrIsBreakAble(self, sLeft:str):
        #     if sLeft == "":
        #         return True
        #     # print(sLeft)
        #     for i in range(1,len(sLeft)+1, 1):
        #         checkIWord = sLeft[:i]
        #         if checkIWord in self.wordDictSet:
        #             if i == len(sLeft):
        #                 return True
        #             if checkStrIsBreakAble(self, sLeft[i:]):
        #                 return True
        #     return False
        # # return checkStrIsBreakAble(self, s)
        # # memo could be replaced by python. cache
        # # self.memo = {}
        # @cache
        # def dp_backtrack(idx):
        #     if idx<0:
        #         return True
        #     # if idx in self.memo:
        #     #     return self.memo[idx]
        #     for word in wordDict:
        #         if s[idx-len(word)+1:idx+1] == word:
        #             if dp_backtrack(idx-len(word)):
        #                 # self.memo[idx] = True
        #                 return True
        #     return False
        # return dp_backtrack(len(s)-1)

        