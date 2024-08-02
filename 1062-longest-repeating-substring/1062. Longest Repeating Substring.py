class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # going through each index i
        # record the substring from all previous char and generate the new substring
        # add them in the set to check if it appeared before, to get the max repeating
        # time: O(N*N) space:O(N*N)
        preStr = [s[0]]
        appeared = set(s[0])
        maxRepeatLen = 0
        for i in range(1,len(s)):
            # create new substr
            preStr.append(s[i])
            for j in range(len(preStr)):
                if j < len(preStr)-1:
                    preStr[j] = preStr[j]+s[i]
                if preStr[j] in appeared:
                    maxRepeatLen = max(maxRepeatLen, len(preStr[j]))
                else:
                    appeared.add(preStr[j])
        return maxRepeatLen


        