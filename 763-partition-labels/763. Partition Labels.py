class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # remember the first occurance of the character
        # using a queue to remember the split, pop out if the previous split location 
        # is later than now
        # time: O(N) space:O(N)
        firstLabel = {}
        splitLoc = []
        for i in range(len(s)):
            nowS = s[i]
            if nowS not in firstLabel.keys():
                firstLabel[s[i]] = i
            else:
                preSplit = firstLabel[s[i]]
                while splitLoc:
                    if splitLoc[-1]>=preSplit:
                        splitLoc.pop()
                    else:
                        break
            splitLoc.append(i)
        # print(splitLoc)
        pre = -1
        ret = []
        for idx in splitLoc:
            ret.append(idx-pre)
            pre = idx
        return ret

        
                
        