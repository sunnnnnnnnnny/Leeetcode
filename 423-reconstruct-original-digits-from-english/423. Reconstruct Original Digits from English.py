class Solution:
    def originalDigits(self, s: str) -> str:
        # getting the possible numbers first from the unique
        # nDict = {"z":["zero"], "o":["one"], "e":["eight"], "n":["nine"]}
        # n2Dict = { "t":["two","three"], "f"["four","five"], "s"["six","seven"]}
        # time:O(N+26) = O(N) space:O(26) for count = O(1)
        charCnt = collections.Counter(s)
        # building digit freq
        out = {}
        out[0] = charCnt['z']
        out[2] = charCnt['w']
        out[4] = charCnt['u']
        out[5] = charCnt['f']-out[4]
        out[6] = charCnt['x']
        out[7] = charCnt['s']-out[6]
        out[8] = charCnt['g']
        out[3] = charCnt['t']-out[2]-out[8]
        out[9] = charCnt['i']-out[8]-out[5]-out[6]
        out[1] = charCnt['o']-out[2]-out[4]-out[0]
        ret = ""
        for i in range(0,10):
            nowStr = str(i)*out[i]
            ret+=nowStr
        return ret