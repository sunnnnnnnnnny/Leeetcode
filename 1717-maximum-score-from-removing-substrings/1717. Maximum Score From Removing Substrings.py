class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Greedy by getting all the possible high pair
        # then get the lower pair
        highPair = ["a","b"]
        lowPair = ["b", "a"]
        if y>x:
            tmp = highPair
            highPair = lowPair
            lowPair = tmp
        def removePair(now, pair):
            writeIdx = 0
            # newStr = now
            for i in range(len(now)):
                now[writeIdx] = now[i]
                writeIdx += 1
                if writeIdx>1 and now[writeIdx-2] == pair[0] and now[writeIdx-1]==pair[1]:
                    writeIdx -= 2
                # if now[i] == pair[-1]:
                #     if writeIdx>0 and newStr[writeIdx-1] == pair[0]:
                #         writeIdx-= 1
                #     else:
                #        newStr[writeIdx] = now[i]
                #        writeIdx+=1
                # else:
                #     newStr[writeIdx] = now[i]
                #     writeIdx+=1
            
            return now[:writeIdx]
        ret = 0
        # str is immutable, thus transition to list
        s = list(s)
        afterHighStr = removePair(s, highPair)
        addCostPairs = (len(s)-len(afterHighStr))//2
        ret += addCostPairs*max(x,y)
        afterLowStr = removePair(afterHighStr, lowPair)
        addCostPairs = (len(afterHighStr)-len(afterLowStr))//2
        ret += addCostPairs*min(x,y)
        # print(afterHighStr, afterLowStr)
        return ret


        # DP backtracking
        # time: O(N^3)=> time out
        # memo = {}
        # def maxGainOfStr(now):
        #     if now == "":
        #         return 0
        #     if now in memo.keys():
        #         return memo[now]
        #     maxRet = 0
        #     for i in range(1, len(now)):
        #         if now[i] == "a" and now[i-1] == "b":
        #             tryChild = now[:i-1]+now[i+1:]
        #             maxRet = max(maxRet, maxGainOfStr(tryChild)+y)
        #         elif now[i] == "b" and now[i-1] == "a":
        #             tryChild = now[:i-1]+now[i+1:]
        #             maxRet = max(maxRet, maxGainOfStr(tryChild)+x)
        #     memo[now] = maxRet
        #     return maxRet
        # return maxGainOfStr(s)
            


        