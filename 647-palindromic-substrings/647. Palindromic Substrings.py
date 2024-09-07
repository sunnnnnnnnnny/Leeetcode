class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force time:O(n^2)
        # to use the previous calculated result, at each char get the previous same char loc
        # if the substring in between is alindronmic, then we find another
        subPalindro = set()
        prevCharLoc = {}
        ret = 0
        for i in range(len(s)):
            if s[i] in prevCharLoc.keys():
                for prevLoc in reversed(prevCharLoc[s[i]]):
                    btwStr = s[prevLoc+1:i]
                    # print(i, s[i], btwStr)
                    if btwStr in subPalindro or btwStr == "":
                        ret+=1
                        subPalindro.add(s[prevLoc:i+1])

            else:
                prevCharLoc[s[i]] = []
                subPalindro.add(s[i])
            ret+=1
            prevCharLoc[s[i]].append(i)
        # print(subPalindro)
        return ret

