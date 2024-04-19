class Solution:
    def hammingWeight(self, n: int) -> int:
        # convert to binary number and directly add one
        # 
        oneCnt = 0
        mask = 1
        for i in range(1, 32, 1):
            if (n&mask) != 0:
                oneCnt+=1
            mask <<= 1
        return oneCnt
        