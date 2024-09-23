class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # group the pairs and count how many it can have
        # key being counter , sorted word
        wordPair = {}
        for w in words:
            wKey = ''.join(sorted(w))
            if wKey not in wordPair.keys():
                wordPair[wKey] = {}
            if w not in wordPair[wKey].keys():
                wordPair[wKey][w] = 0
            wordPair[wKey][w]+=1
        def ifSelfPalindrome(w):
            return w[0] == w[1]
        pairCnt = 0
        centeral = False
        for key, val in wordPair.items():
            selfPali = ifSelfPalindrome(key)
            if selfPali:
                # cc and xx can't be a parlidrome, thus need to consider the centeral
                if val[key]%2 == 0:
                    pairCnt += val[key]
                else:
                    pairCnt += val[key]-1
                    centeral = True
            else:
                parC = inf if len(val)==2 else 0
                for k in val.keys():
                    parC = min(parC, val[k])
                pairCnt += (parC)*2
        if centeral:
            pairCnt+=1
        
        return pairCnt*2
