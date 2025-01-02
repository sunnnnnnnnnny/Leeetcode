class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # sliding window method
        volCnt = defaultdict(int)
        l = 0
        r = 0
        cnt = 0
        def isVolSub(volCnt):
            if len(volCnt.keys())<5:
                return False
            for k,v in volCnt.items():
                if v<1:
                    return False
            return True
        while r<len(word):
            if word[r] in ['a', 'e', 'i', 'o', 'u']:
                volCnt[word[r]]+=1
                # print(r, volCnt)
                # print(r, isVolSub(volCnt))
                tmpVolCnt = copy.deepcopy(volCnt)
                tmpL = l
                while isVolSub(tmpVolCnt) and tmpL<r-3:
                    cnt+=1
                    tmpVolCnt[word[tmpL]]-=1
                    tmpL += 1
            else:
                # shrink the left and clean volcnt
                l = r+1
                volCnt = defaultdict(int)
            r+=1
        return cnt
