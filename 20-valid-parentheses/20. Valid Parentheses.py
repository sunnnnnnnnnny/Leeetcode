class Solution:
    def isValid(self, s: str) -> bool:
        # using FILO queue to record the open bracket
        # once meeting the close bracket, pop the last open one
        # check if the type is correct, and at the end if open queue>0
        # TIme; O(N) traverse the str with each pop cost O(1)
        # Space:O(N) max all open bracket goes into the queue
        # or convert the open bracket as close brackt str, 
        # and move the pointers when meeting one close, to verify the validtion
        # Time: O(N) Space:O(N)
        open = deque()
        # def getCloseBracket(char):
        #     if char == '(' :
        #         return ')'
        #     elif char =='{' :
        #         return '}'
        #     elif char == '[':
        #         return ']'
        #     return ''
        bracketMap = {
            '{':'}',
            '(':')',
            '[':']'
        }
        for char in s:
            if char in ('(' , '{', '['):
                open.append(char)
            elif char in (')', '}', ']'):
                if len(open)==0:
                    return False
                lastOpen = open.pop()
                # shouldClose = getCloseBracket(lastOpen)
                if bracketMap[lastOpen] != char:
                    return False
            else:
                return False
        return len(open) == 0
        