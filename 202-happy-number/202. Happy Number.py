class Solution:
    def isHappy(self, n: int) -> bool:
        # record the seen number so we can detected the loop
        # the max next of number with 13 digits would be 1053, and 4 digit max next is 243
        # therefore we mostly would store 243 numbers-> space:O(logN) or O(1)
        # the cost of finding next num is O(logN)
        # thus total time cost is logN+log logN+ log log logN+...
        # time: O(logN) space:O(logN)
        # second way is by fast and slow pointer
        # when slow == fast, meaning theres a loop
        # time:O(logN) space:O(1)
        seen = set()
        def calculateHappy(num):
            if num == 1:
                return True
            if num in seen:
                return False
            seen.add(num)
            nextNum = 0
            while num>0:
                digit = num%10
                nextNum += (digit*digit)
                num = num//10
            return calculateHappy(nextNum)
        return calculateHappy(n)
        