class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # record the positive and negative product upto now
        # reset when meet 0
        # time: O(n) space:O(1)
        pos = neg = 0
        maxProd = nums[0]
        maxN = nums[0]
        for n in nums:
            if n == 0:
                pos = neg = 0
            else:
                pos = n if pos==0 else pos*n
                neg = 0 if neg == 0 else neg*n
            if pos<neg:
                temp = pos
                pos = neg
                neg = temp
            maxProd = max(maxProd, pos)
            maxN = max(maxN, n)
        return maxProd if maxProd!=0 and maxProd>maxN else maxN


