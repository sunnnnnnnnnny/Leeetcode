class Solution:
    def reverseParentheses(self, s: str) -> str:
        # putting the str of each ( in to the stack
        # meeting the ) pop it and put it back reversed
        # time:O(N) space:O(N)
        start=0
        end = 0
        stackStr = []
        for i in range(len(s)):
            if s[i] == "(":
                now = s[start:i]
                if len(now)>0:
                    stackStr.append(now)
                stackStr.append("(")
                start = i+1
            elif s[i] == ")":
                # need to detail with the str not pushed yet
                leftStr = s[start:i]
                revertStr = leftStr[::-1]
                while stackStr:
                    if stackStr[-1] == "(":
                        break
                    else:
                        addStr = stackStr.pop()
                        revertStr += addStr[::-1]
                if stackStr and stackStr[-1] == "(":
                    stackStr.pop()
                stackStr.append(revertStr)
                start = i+1
            else:
                # add the last part back
                if i == len(s)-1:
                    now = s[start:]
                    if len(now)>0:
                        stackStr.append(now)
        ret = ""
        while stackStr:
            ret += stackStr.pop(0)
        return ret
        