class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # the solution doesn't need to take care of the maxLetter as it's just a distrction
        # since a string having occurences of x times, the substring of it will also having the x occurence 
        # therefore to fullfill the need of minSize
        # we just count the frequency of any substring with minSize
        # then the max occurence is the answer
        minsizeSubstr = {}
        ret = 0
        charFreq = {}
        for i in range(minSize):
            if s[i] not in charFreq.keys():
                charFreq[s[i]] = 0
            charFreq[s[i]] += 1
        for i in range(len(s)-minSize+1):
            if i>0:
                if i+minSize-1<len(s): 
                    if s[i+minSize-1] not in charFreq.keys():
                        charFreq[s[i+minSize-1]] = 0
                    charFreq[s[i+minSize-1]] += 1
                charFreq[s[i-1]] -= 1
                if charFreq[s[i-1]] == 0:
                    del charFreq[s[i-1]]

            subStr= s[i:i+minSize]
            if subStr not in minsizeSubstr.keys():
                minsizeSubstr[subStr] = 0
            minsizeSubstr[subStr] += 1
            if len(charFreq.keys())<=maxLetters:
                ret = max(ret, minsizeSubstr[subStr])
        return ret

        # count the unique letters in the window, always have it to maxLetters
        # once find based on the minSize&maxSize to count it
        # time:O(N*(maxS-minS)) b/c for every valid substring, we will check it for the maxSize &minSize
        # space:O(N) for temp storing the frequency
        # charCnt = {}
        # subStrCnt = {}
        # start = 0
        # ret = 0
        # for i in range(len(s)):
        #     if s[i] not in charCnt.keys():
        #         charCnt[s[i]] = 0
        #     charCnt[s[i]] += 1
        #     curLen = i-start+1
        #     # print(i, start, curLen, charCnt, subStrCnt)
        #     if curLen>maxSize:
        #         for j in range(start, i-maxSize+1):
        #             charCnt[s[j]] -= 1
        #             if charCnt[s[j]] ==0:
        #                 del charCnt[s[j]]
        #         start = i-maxSize+1

        #     curLen = i-start+1
        #     # print(i, start, charCnt)
        #     if len(charCnt.keys()) <= maxLetters and curLen>=minSize:
        #         subStr = s[start:i+1]
        #         if subStr not in subStrCnt.keys():
        #             subStrCnt[subStr] = 0
        #         subStrCnt[subStr] += 1
        #         ret = max(ret, subStrCnt[subStr])
        #         # cnt the ending with this position i which fits to minSize
        #         removedCnt = {}
        #         removedChars = 0
        #         for j in range(start, i-minSize+1):
        #             removeIdx = j
        #             # print(removeIdx, s[removeIdx], charCnt)
        #             if s[removeIdx] not in removedCnt.keys():
        #                 removedCnt[s[removeIdx]] = 0
        #             removedCnt[s[removeIdx]] += 1
        #             if charCnt[s[removeIdx]]==removedCnt[s[removeIdx]]:
        #                 removedChars += 1
        #             if len(charCnt.keys()) - removedChars <= maxLetters:
        #                 subStr = s[removeIdx+1:i+1]
        #                 if subStr not in subStrCnt.keys():
        #                     subStrCnt[subStr] = 0
        #                 subStrCnt[subStr] += 1
        #                 ret = max(ret, subStrCnt[subStr])
        #             else:
        #                 break
        #     elif len(charCnt.keys()) > maxLetters and curLen>=minSize:
        #         # check if smaller size could have the smaller count
        #         newStart = start
        #         # print("larger ", i, start, charCnt)
        #         for j in range(start, i-minSize+1):
        #             removeIdx = j
        #             # print(removeIdx, s[removeIdx], charCnt)
        #             charCnt[s[removeIdx]] -= 1
        #             if charCnt[s[removeIdx]] ==0:
        #                 del charCnt[s[removeIdx]]
        #             newStart = j+1
        #             if len(charCnt.keys()) <= maxLetters:
        #                 subStr = s[removeIdx+1:i+1]
        #                 if subStr not in subStrCnt.keys():
        #                     subStrCnt[subStr] = 0
        #                 subStrCnt[subStr] += 1
        #                 ret = max(ret, subStrCnt[subStr])
        #                 break
        #         start = newStart
        #         # print("new larger ", i, start, charCnt)
        #         if len(charCnt.keys()) <= maxLetters:
        #             removedCnt = {}
        #             removedChars = 0
        #             for j in range(start, i-minSize+1):
        #                 if s[j] not in removedCnt.keys():
        #                     removedCnt[s[j]] = 0
        #                 removedCnt[s[j]] += 1
        #                 if charCnt[s[j]]==removedCnt[s[j]]:
        #                     removedChars += 1
        #                 if len(charCnt.keys()) - removedChars <= maxLetters:
        #                     subStr = s[j+1:i+1]
        #                     if subStr not in subStrCnt.keys():
        #                         subStrCnt[subStr] = 0
        #                     subStrCnt[subStr] += 1
        #                     ret = max(ret, subStrCnt[subStr])
        #                 else:
        #                     break

        # # print(subStrCnt)
        # return ret