class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # pack greedy thus try to have as many word as possible
        # count the words of each line, and have the space distruibute
        # mimic the greedy time:O(N) space:O(1)
        ret= []
        i=0
        while i<=len(words)-1:
            start = i
            nowLength = len(words[start])
            # print(start, nowLength)
            while nowLength<=maxWidth and i<len(words)-1:
                i += 1
                # at least one space in btw words
                nowLength+=(1+len(words[i]))
            if nowLength>maxWidth:
                linWords = i-start
                wordSize = nowLength-1-len(words[i])-(linWords-1)
                spaceSize = (maxWidth-wordSize)
                if linWords-1>0:
                    spaceSize = (maxWidth-wordSize)//(linWords-1)
                # how many more extraSpace from the left needed to add
                extraSpace = maxWidth-wordSize-(spaceSize*(linWords-1))
                # print(start, i, linWords, wordSize, spaceSize, extraSpace)
                line = []
                for j in range(start, i):
                    line.append(words[j])
                    if j < i-1:
                        curSpaceSize = spaceSize
                        if extraSpace>0:
                            curSpaceSize+=1
                            extraSpace -=1
                        line.append(" "*curSpaceSize)
                if linWords == 1:
                    line.append(" "*spaceSize)
                ret.append("".join(line))
            else:
                # put single space and the rest ad spaces
                line = []
                restSpace = maxWidth
                for j in range(start, i+1):
                    newWord = words[j]
                    restSpace -= len(newWord)
                    if restSpace>0:
                        newWord = words[j]+" "
                        restSpace -= 1
                    line.append(newWord)
                if restSpace>0:
                    line.append(" "*restSpace)
                ret.append("".join(line))
                i+=1
        return ret
