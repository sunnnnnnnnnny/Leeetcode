class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # simulate the process, will take a long time O(N^2)
        ls = [s[i] for i in range(len(s))]
        def findZO(listIn, n):
            for i in range(1, n):
                if listIn[i]=='1' and listIn[i-1]=='0':
                    return True
            return False
        n = len(s)
        cnt = 0
        while findZO(ls, n):
            newLs = ls[:]
            cnt += 1
            for i in range(1, n):
                if ls[i]=='1' and ls[i-1]=='0':
                    newLs[i]='0'
                    newLs[i-1]='1'
            ls = newLs
        return cnt
