class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # based on the requriement then do conversion, 
        # time:O(n+2n+kn) only the first time would have digit at most 2n size
        # space:O(n)
        now = 0
        # k>=1
        for i in range(len(s)):
            c = ord(s[i])-ord('a')+1
            now += ((c//10)+(c%10))
        
        for l in range(k-1):
            temp = now
            now = 0
            while temp>0:
                now += temp%10
                temp = temp//10
        return now

        