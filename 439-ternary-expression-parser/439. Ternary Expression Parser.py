class Solution:
    def parseTernary(self, expression: str) -> str:
        # stack with the ? pair with :
        # time:O(N) space:O(N)
        eva = []
        i = len(expression)-1
        def evalRet(exp, prev, now):
            # print(exp, prev, now)
            if exp == 'T':
                return prev
            return now
        while i>=0:
            if expression[i] == '?':
                prev = eva.pop()
                now = eva.pop()
                eva.append(evalRet(expression[i-1], prev, now))
                i-=1
            elif expression[i] == ':':
                i-=1
                continue
            else:
                eva.append(expression[i])
            i-=1
        return eva[0]
