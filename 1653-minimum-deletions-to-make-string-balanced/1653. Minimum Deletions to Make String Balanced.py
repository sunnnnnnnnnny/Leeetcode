class Solution:
    def minimumDeletions(self, s: str) -> int:
        # greedy
        # find each indxe, of a before it and b after it
        # the min delete is by getting the max of sum im step 2
        # time:O(N) space(2N)
        # second way is one pass as we don't delete the a on left but b on right
        # by delete the b on left and a on right will be the min deletion
        # time :O(N) space: O(1)
        n = len(s)
        aTotal = sum(1 for ch in s if ch == 'a')
        aRight = aTotal
        bLeft = 0
        minDelete = n
        for ch in s:
            if ch == 'a':
                aRight -= 1
            minDelete = min(minDelete, aRight+bLeft)
            if ch == 'b':
                bLeft += 1
        return minDelete
        # aCount = [0]*len(s)
        # bCount = [0]*len(s)
        # for i in range(0,len(s), 1):
        #     reverseI = len(s)-1-i
        #     aCount[i] = aCount[i-1] if i>0 else 0
        #     bCount[reverseI] = bCount[reverseI+1] if i>0 else 0
        #     if s[i] == 'a':
        #         aCount[i] +=1 
        #     if s[reverseI] == 'b':
        #         bCount[reverseI] +=1
        # maxAB = 0
        # # print(aCount)
        # # print(bCount)
        # for i in range(0,len(s), 1):
        #     nowAB = aCount[i]+bCount[i]
        #     maxAB = max(maxAB, nowAB)
        # return len(s)-maxAB