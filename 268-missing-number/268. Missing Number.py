class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we can sort it and traverse O(nlogn+N)
        # 2. use hash map => O(N)
        # 3. Xor all the numbers and enum 0~n, b/c i xor i is 0
        # 4 Gauss, just sum all num and the remain of n*(n+1)/2 is the missing
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i
        