class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # by greedyly match the valid match
        # everytime the find the valid pair, then pop it to make the sentence
        # time:O(N) space:O(N)
        openCnt = 0
        retArr = []
        for i in range(len(s)):
            if s[i] == '(':
                openCnt+=1
                retArr.append(s[i])
            elif s[i] == ')':
                if openCnt==0:
                    continue
                openCnt -= 1
                mergeW = s[i]
                while retArr:
                    now = retArr.pop()
                    mergeW = now+mergeW
                    if now == '(':
                        break
                retArr.append(mergeW)
            else:
                retArr.append(s[i])
        ret = ""
        while retArr:
            now = retArr.pop()
            # any left over ( should be ignored
            if now == '(':
                continue
            ret = now+ret
        return ret