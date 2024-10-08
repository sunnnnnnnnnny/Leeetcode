class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # since we want the same digit, meaning by switching the digit
        # if we can find a larger one, then get the min of it
        # brute force:O(N^2) for trying every pair
        # swap the digit if i<j and digit[i]<digit[j] find the smallest pair to do so
        # with the min i, time:O(N) space:O(1)
        digit = []
        while n>0:
            nowD = n%10
            digit.append(nowD)
            n = n//10
        i = j = 0
        # print(digit)
        swapI = -1
        while j<len(digit):
            if digit[i] > digit[j]:
                # the first decrement element
                swapI = j
                break
            elif digit[i] < digit[j]:
                i = j
            else:
                j+=1
        if swapI == -1:
            return -1
        # select the smallest number that's larger than I, 
        # and have the rest in increasing order, by reversing it
        swapJ = -1
        # because it's increasing, find the smallest one would work
        for j in range(swapI-1, -1, -1):
            if digit[j]>digit[swapI]:
                swapJ = j
            else:
                break
        # print(digit)
        # print(swapI, swapJ)
        temp = digit[swapI]
        digit[swapI] = digit[swapJ]
        digit[swapJ] = temp
        # print(digit)
        ret = 0
        tenMuti = 1
        for i in range(swapI-1, -1, -1):
            ret += digit[i]*tenMuti
            tenMuti  = tenMuti*10
        for i in range(swapI,len(digit)):
            ret += digit[i]*tenMuti
            tenMuti  = tenMuti*10
        # print(ret)
        return ret if ret<=2147483647 else -1

