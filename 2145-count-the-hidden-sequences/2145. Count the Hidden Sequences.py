class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # (wrong)taking num in low to up as the start, making it the backtracking
        # using min and max to check the possible sequence
        # time:O(N) space:O(1)
        cur = 0
        minC = cur
        maxC = cur
        for i in differences:
            cur += i
            minC = min(minC, cur)
            maxC = max(maxC, cur)
        diff = upper-lower
        posible = diff - (maxC-minC)
        # print(diff, posible, minC, maxC)
        ret = 0 if posible<0 else posible+1
        return ret