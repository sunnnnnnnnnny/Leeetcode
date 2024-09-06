class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # to record the appeared character's prev location
        # if the end character loc is no in the window, then it's legit
        # otherwise we need to shrink the window
        # time:O(N) space:O(N) if we do not limit the character to 26 eng ones
        start = -1
        appear = {}
        maxLen = 0
        for end in range(len(s)):
            if s[end] in appear.keys() and appear[s[end]]>start:
                start = appear[s[end]]
            curLen = end-start
            maxLen = max(maxLen, curLen)
            appear[s[end]] = end
        return maxLen

