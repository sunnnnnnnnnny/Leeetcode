class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # a^2+b^2+2ab = (a+b)^2
        # a^2+b^2 = (a+b)^2-2ab = c
        # getting the sqrt, time: sqrt(c)*log(c) space:O(1)
        # We iterate over c values for choosing a. For every a chosen, 
        # finding square root of c−a^2 takes O(logc) time in the worst case.
        a = 0
        while a*a <=c:
            b = (c-a*a)**0.5
            if b == int(b):
                return True
            a += 1
        return False