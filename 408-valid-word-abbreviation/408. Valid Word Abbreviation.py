class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # non-adjacent and non-empty substring can be abbr
        # check charcter by character with original and abbr
        # no leading zero
        # if the number doens't match it's false
        # time: O(N)
        oriIdx = 0
        numStr = ""
        for i in range(len(abbr)):
            if oriIdx>=len(word):
                return False
            if abbr[i].isnumeric():
                if (i==0 or not abbr[i-1].isnumeric()):
                    if abbr[i]=="0":
                        return False
                numStr = numStr+abbr[i]
            else:
                if i>0 and abbr[i-1].isnumeric():
                    preLen = int(numStr)
                    if oriIdx+preLen>=len(word):
                        return False
                    else:
                        oriIdx+=preLen
                    numStr = ""
                if abbr[i] != word[oriIdx]:
                    return False
                oriIdx+=1
        if len(numStr)>0:
            preLen = int(numStr)
            oriIdx+=preLen
        if oriIdx!=len(word):
            return False
        return True

                


        