class Solution:
    def maximumSwap(self, num: int) -> int:
        # record each digit's rightmost idx
        # checking the digit from left and swap the possible largest dight from the right
        # making the most of the digit
        # Greedy time:O(N)
        # space: O(1) b/c to record the digit's rightmost idx
        # but spliting the num to str is O(N)
        ret = num
        numStr = str(num)
        smallestLeft = 0
        left = 0
        largestRight = len(numStr)-1
        right = len(numStr)-1
        # record the rightmost Idx of each digit
        numR2Idx = [-1 for _ in range(10)]
        while right>=0:
            if numR2Idx[int(numStr[right])] == -1:
                numR2Idx[int(numStr[right])] = right
            right -= 1
        print(numR2Idx)
        while left<len(numStr)-1:
            for i in range(9,int(numStr[left]),-1):
                if numR2Idx[i] != -1 and numR2Idx[i]>left:
                    temp = list(numStr)
                    temp[left] = str(i)
                    temp[numR2Idx[i]] = numStr[left]
                    ret = max(ret, int(''.join(temp)))
                    return ret
            left += 1

        return ret
            