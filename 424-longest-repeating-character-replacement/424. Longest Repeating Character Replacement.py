class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char2Freq = {}
        start = end = 0
        maxFreq = 0
        maxLen = 0
        while end<len(s):
            if s[end] not in char2Freq.keys():
                char2Freq[s[end]] = 0
            char2Freq[s[end]] += 1
            maxFreq = max(char2Freq[s[end]], maxFreq)
            if end-start+1-maxFreq<=k:
                maxLen = max(maxLen, end-start+1)
                # print(start, end, maxFreq)
            else:
                while start<end:
                    char2Freq[s[start]]-=1
                    start += 1
                    maxFreq = max(char2Freq.values())
                    if end-start+1-maxFreq<=k:
                        # print(start, end, char2Freq)
                        break
            end+=1
        return maxLen

        # by not considering the fix letter, and only the window size
        # the valid str len is end-start+1-maxFreq<=k
        # we can move the start pointer to right when the window is not valid
        # by this approach we are only going through it once
        # time: O(N)
        # Space: O(M) for frequency storage
        # start = 0
        # freqMap = {}
        # maxFreq = 0
        # ret = 0
        # for end in range(len(s)):
        #     freqMap[s[end]] = freqMap.get(s[end], 0)+1
        #     # the only freq will change is the freqMap[s[end]]
        #     # thus comparing the maxFreq is only necessary with the end letter
        #     maxFreq = max(maxFreq, freqMap[s[end]])

        #     isValid = (end-start+1-maxFreq<=k)
        #     if not isValid:
        #         freqMap[s[start]]-=1
        #         start+=1
        #     ret = end-start+1
        # return ret

        # taking each single letter as fixed to search possible valid str
        # by sliding window of checking the substr
        # time: O(N*M) n is the length of s, M is the unique letters
        # space: O(M)
        # uniLetter = set(s)
        # maxLen = 0
        # def isWindowValid(start, end, count, k):
        #     return end-start+1-count<=k
        # for fixLetter in uniLetter:
        #     start = 0
        #     count = 0
        #     for end in range(len(s)):
        #         if s[end] == fixLetter:
        #             count+=1
        #         while not isWindowValid(start, end, count, k):
        #             if s[start]==fixLetter:
        #                 count-=1
        #             start+=1
        #         maxLen = max(maxLen, end-start+1)
        # return maxLen
                