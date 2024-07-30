class Solution:
    def minimumDeletions(self, s: str) -> int:
        # greedy
        # find each indxe, of a before it and b after it
        # the min delete is by getting the max of sum im step 2
        # time:O(N) space(2N)
        aCount = [0]*len(s)
        bCount = [0]*len(s)
        for i in range(0,len(s), 1):
            reverseI = len(s)-1-i
            aCount[i] = aCount[i-1] if i>0 else 0
            bCount[reverseI] = bCount[reverseI+1] if i>0 else 0
            if s[i] == 'a':
                aCount[i] +=1 
            if s[reverseI] == 'b':
                bCount[reverseI] +=1
        maxAB = 0
        # print(aCount)
        # print(bCount)
        for i in range(0,len(s), 1):
            nowAB = aCount[i]+bCount[i]
            maxAB = max(maxAB, nowAB)
        return len(s)-maxAB