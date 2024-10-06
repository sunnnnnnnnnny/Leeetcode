class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # should be able to find only 2 different char at 2 pos
        # where the s1[i] == s2[j], then it's possitble
        # time:O(2N) space:O(1)
        if len(s1)!=len(s2):
            return False
        if s1 == s2:
            return True
        diffPair = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diffPair.append((s1[i],s2[i]))
                if len(diffPair)>2:
                    return False
        if len(diffPair)!=2:
            return False
        if diffPair[0][0] == diffPair[1][1] and diffPair[0][1] == diffPair[1][0]:
            return True
        return False
        