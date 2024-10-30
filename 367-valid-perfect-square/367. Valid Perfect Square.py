class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # break into odd or even, for even calculate it's the power of 2
        # odd will check if it's 1,3,5... square
        # time:O()
        def evenCnt(num):
            twoCnt = 0
            while num%2 == 0:
                num = num//2
                twoCnt += 1
            twoSquare = True if twoCnt%2 == 0 else False
            return twoSquare, num
        def oddCheck(num):
            i = 1
            double = i*i
            while double<=num:
                if double==num:
                    return True
                i+=2
                double = i*i
            return False
        if num%2 == 0:
            evenGood, leftN = evenCnt(num)
            if not evenGood:
                return False
            return oddCheck(leftN)
        return oddCheck(num)