class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window, expand if the substr doesn't cover thewindow
        # once it covers shrink the window until it's not valid
        # time:O(N) space:O(N) for keeping the record to verify substr validate
        start = 0
        subCharCnt = {}
        for i in range(len(t)):
            if t[i] not in subCharCnt.keys():
                subCharCnt[t[i]] = 0
            subCharCnt[t[i]]+=1
        def subStrValid(cntDict):
            for key, val in cntDict.items():
                if val>0:
                    return False
            return True
        minLenStr = ""
        for end in range(len(s)):
            if s[end] in subCharCnt.keys():
                    subCharCnt[s[end]]-=1
            while subStrValid(subCharCnt) and start<=end:
                curSubStr = s[start:end+1]
                if minLenStr == "" or len(minLenStr)>len(curSubStr):
                    minLenStr = curSubStr
                if s[start] in subCharCnt.keys():
                    subCharCnt[s[start]]+=1
                start +=1
        return minLenStr
            

