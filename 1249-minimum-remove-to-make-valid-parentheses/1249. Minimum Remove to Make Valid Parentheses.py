class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # using a queue for each left pos, if the right can make left a pair
        # then the string will be valid until the next left
        # time:O(2N) space:O(N)
        leftQ = []
        leftCnt = 0
        ret = ""
        # print(s, len(s))
        for i in range(len(s)):
            # print(i, leftCnt, leftQ)
            if s[i] == ')':
                if leftCnt>0:
                    leftQ.append(s[i])
                    while leftQ:
                        now = leftQ.pop(0)
                        ret += now
                        if now == '(':
                            leftCnt -= 1
                            break
            else:
                if s[i] == '(':
                    leftCnt+=1
                leftQ.append(s[i])
        while leftQ:
            now = leftQ.pop(0)
            if now == '(':
                continue
            ret += now
        return ret
                