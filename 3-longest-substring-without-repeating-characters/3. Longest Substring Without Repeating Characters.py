class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using dict to record the nonrepeat char with their idx
        # the len of the set is the cnt
        # Time: O(N) space:O(N) for dict
        # another method is to use list of [0,26] as A-Z since it's fixed char

        nonRepeat = {}
        maxLen = 0
        startIdx = 0
        for i in range(len(s)):
            if s[i] not in nonRepeat:
                nonRepeat[s[i]] = i
            else:
                nowLen = i-startIdx
                maxLen = max(maxLen, nowLen)
                oriIdx = nonRepeat[s[i]]
                for clearIdx in range(startIdx, oriIdx+1, 1):
                    del nonRepeat[s[clearIdx]]
                startIdx = oriIdx+1
                nonRepeat[s[i]] = i
            # print('i: startIdx:', i, startIdx)
            # print(nonRepeat)
        # print(nonRepeat)
        nowLen = len(s)-startIdx
        maxLen = max(maxLen, nowLen)
        return maxLen
        