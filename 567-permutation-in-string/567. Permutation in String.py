class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # as permutation of s1 in s2
        # we could use the counter of each char to identify if partially correct
        # a:1 b:1
        # s2=aab 0 a:1 1 a:2 not fit, start = 0->1 
        # time:O(N) N  = len(s2)
        # space: O(2M) M =len(s1)
        if len(s1)>len(s2):
            return False
        s1Freq = collections.Counter(s1)
        curFreq = {}
        start=0
        for end in range(len(s2)):
            # as permutation shouldn't include other char and need to reset the counter
            if s2[end] not in s1Freq.keys():
                start = end+1
                curFreq = {}
                continue
            if s2[end] not in curFreq.keys():
                curFreq[s2[end]] = 0
            curFreq[s2[end]] += 1
            while curFreq[s2[end]]>s1Freq[s2[end]]:
                curFreq[s2[start]] -= 1
                start+=1
            # print(start, end, curFreq)
            if end-start+1 == len(s1):
                return True
        return False
            
        