class Solution:
    def isValid(self, s: str) -> bool:
        # push all the open into queue, everything meets a close pop one
        # and check if it match the set, time:O(n) space:O(n)
        # assume no other type of input included
        openB = []
        def getMatch(openOne):
            if openOne == '(':
                return ')'
            elif openOne == '[':
                return ']'
            return '}'
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                matchClose = getMatch(s[i])
                openB.append(matchClose)
            else:
                # FILO is pop(), FIFO is pop(0)
                if len(openB)==0:
                    return False
                latestClose = openB.pop()
                if latestClose != s[i]:
                    return False
        return True if len(openB)==0 else False
