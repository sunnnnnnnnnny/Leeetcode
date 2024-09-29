class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # using sliding window to make sure the window is alway with k unuque char
        # time:O(N) space:O(N) as we record the unique keys in the window
        if k == 0:
            return 0
        containChar = {}
        left = 0
        ret = 0
        for i in range(len(s)):
            if s[i] not in containChar.keys():
                containChar[s[i]] = 0
            containChar[s[i]] += 1
            if len(containChar.keys())>k:
                while left<i:
                    removeK = s[left]
                    containChar[removeK]-=1
                    left += 1
                    if containChar[removeK] == 0:
                        del containChar[removeK]
                        break
            nowLen = i-left+1
            ret = max(ret, nowLen)
        return ret

                