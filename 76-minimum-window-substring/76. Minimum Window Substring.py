class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # start to expand the window until it's valid to cover the whole t, then shrink it to min,
        # then move the window with this size, once find another valid window start to shrink
        # char in t is m max 26, s size is n. time:O(s+t) space:O(s+t)
        hashT = collections.Counter(t)
        start = 0
        ret = ""
        minLen = len(s)
        def validCover(hashT):
            leftNeedCharCnt = 0
            for v in hashT.values():
                leftNeedCharCnt += v if v>=0 else 0
            return True if leftNeedCharCnt == 0 else False
        for i in range(len(s)):
            c = s[i]
            if c in hashT:
                hashT[c] -= 1
            if validCover(hashT):
                # try to shrink
                while start<i:
                    startC = s[start]
                    if startC in hashT:
                        hashT[startC] += 1
                    if validCover(hashT):
                        start += 1
                    else:
                        if startC in hashT:
                            hashT[startC] -= 1
                        break
                nowLen = (i-start+1)
                ret = s[start:i+1] if minLen>=nowLen else ret
                minLen = min(minLen, nowLen)
            else:
                if ret != "":
                    start += 1
        return ret
