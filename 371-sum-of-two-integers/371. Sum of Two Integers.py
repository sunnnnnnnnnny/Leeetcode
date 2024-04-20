class Solution:
    def getSum(self, a: int, b: int) -> int:
        # by using xor and deal with carry over the over way
        # didn't master this one too hard
        x, y = abs(a), abs(b)
        # to ensure we deal with x>= y
        if x<y:
            return self.getSum(b,a)
        sign = 1 if a>0 else -1
        if a*b >=0:
            # sum of two possible int
            while y:
                x, y = x^y, (x&y)<<1
        else:
            # difference of 2 positive int
            while y:
                x, y = x^y, ((~x)&y)<<1
        #  take back the sign
        return x*sign
        