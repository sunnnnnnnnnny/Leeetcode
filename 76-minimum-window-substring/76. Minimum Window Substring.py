class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # by sliding window we could first find the valid substr including t
        # first expanding the end 
        # then shrik the start to keep it valid
        # time: O(M+N)
        # Space: O(M+N)
        reqFreq = {}
        for needChar in t:
            reqFreq[needChar] = reqFreq.get(needChar, 0)+1
        # print(reqFreq)
        def isValid(nowFreq, needFreq):
            for key in needFreq:
                nowF = nowFreq.get(key, 0)
                if nowF<needFreq[key]:
                    return False
            return True
        start = 0
        ret = ""
        nowFreq = {}
        for end in range(len(s)):
            nowFreq[s[end]] = nowFreq.get(s[end], 0)+1
            if isValid(nowFreq, reqFreq):
                # move start
                while start<=end and isValid(nowFreq, reqFreq):
                    nowFreq[s[start]]-=1
                    start +=1
                # cause the start had already moved one step away being valid
                nowLen = end-start+1+1
                if len(ret)==0 or nowLen<len(ret):
                    ret = s[start-1:end+1]
        return ret

        