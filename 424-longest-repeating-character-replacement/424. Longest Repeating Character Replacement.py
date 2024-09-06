class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # since we can exchange any character to wanted one
        # to use the least cost is by changing all other character to the high freq
        # the longest substring len would be high freq len+k
        # sliding window to expand when k>strLen-highFreqLen
        # need to record the currrent window freq
        # time:O(N) space:O(N) to record the freq
        freq = {s[0]:1}
        maxfKey=s[0]
        start=end=0
        maxLen = 0
        while end<len(s):
            curLen = end-start+1
            # print(start, end, maxfKey)
            if curLen-freq[maxfKey]<=k:
                # only the substr is valid can be consider as maxLen
                maxLen = max(curLen, maxLen)
                end+=1
                if end>=len(s):
                    break
                if s[end] not in freq.keys():
                    freq[s[end]] = 0
                freq[s[end]] +=1
                if freq[maxfKey]<freq[s[end]]:
                    maxfKey = s[end]
            else:
                freq[s[start]]-=1
                start +=1
                maxfKey = max(freq, key= lambda x:freq[x])
        return maxLen
                