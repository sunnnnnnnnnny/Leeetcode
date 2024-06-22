class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottomup the dp
        # dp[i]=any(s[i - word.length + 1, i]==word && dp[i - word.length])
        # Given n as the length of s, m as the length of wordDict, and k as the average length of the words in wordDict,
        # time; O(n*m*k)
        # space: O(N) for the dp array
        N = len(s)
        dp = [False]*(N+1)
        # we record the result of i at i+1 dp
        # with the dp[0] as base being True
        dp[0] = True
        for i in range(1,N+1):
            # check at each index if the i-wordlength can make a thing
            for word in wordDict:
                # the word will start at i-len(word)+1 and end at i which should state i+1
                if i-len(word)>=0 and s[i-len(word):i] == word:
                    dp[i] = dp[i] or dp[i-len(word)]
                    # print(i, word, dp[i])
        return dp[-1]



        # backtracking
        # time: O(N^2+M*K)
        # space:O(N+M*K) N for stack and m*K for the words (Trie)
        # memo = {}
        # for word in wordDict:
        #     memo[word] = True
        # def backTrack(leftS:str):
        #     if len(leftS) == 0:
        #         return True
        #     if leftS in memo.keys():
        #         return memo[leftS]
        #     ans = False
        #     for i in range(len(leftS)-1, -1, -1):
        #         if leftS[i:] in memo.keys() and memo[leftS[i:]] == True:
        #             ret = backTrack(leftS[:i])
        #             if ret == True:
        #                 ans = True
        #                 break
        #     memo[leftS] = ans
        #     return ans
        # ans = backTrack(s)
        # return ans


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

        