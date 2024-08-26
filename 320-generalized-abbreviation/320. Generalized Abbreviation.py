class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # dp back tracking , every char can be abb or not
        # time: O(2^len(word)) space = time
        ret = []
        wordLen = len(word)
        def genAbb(nowIdx, abbCnt, lastAbbIdx, prefix):
            nonlocal ret, word, wordLen
            if nowIdx == wordLen:
                if abbCnt>0:
                    prefix += str(abbCnt)
                ret.append(prefix)
                return
            # select add as abbr or not
            if abbCnt > 0:
                # be abb
                genAbb(nowIdx+1, abbCnt+1, lastAbbIdx, prefix)
                # not
                if abbCnt>0:
                    prefix+=str(abbCnt)
                newPrefix = prefix+word[nowIdx]
                genAbb(nowIdx+1, 0, lastAbbIdx, newPrefix)
            else:
                if lastAbbIdx<nowIdx-1:
                    genAbb(nowIdx+1, abbCnt+1, nowIdx, prefix)
                
                # not
                if abbCnt>0:
                    prefix+=str(abbCnt)
                newPrefix = prefix+word[nowIdx]
                genAbb(nowIdx+1, 0, lastAbbIdx, newPrefix)
        genAbb(0,0,-2,"")
        return ret
                



        