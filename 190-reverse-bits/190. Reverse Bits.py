class Solution:
    def reverseBits(self, n: int) -> int:
        # having a 32 bit 1 unsigned num, then xor with n
        # the remain is the reverse num
        # correct: the reverse int is mirror of the int
        ret = 0
        power = 31
        while n:
            ret += (n&1)<<power
            n = n>>1
            power -= 1
        return ret
        