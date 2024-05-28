class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # sort the array then traverse the array to check if such x exist
        # time: O(NlogN+N) space:O(1)?
        # the max x can be is N
        # keep record of how many num is larger than 0-N in the array
        # traverse the array once then check the record
        # time: O(N+N) spcae:O(N)
        N = len(nums)
        record = [0]*(N+1)
        for num in nums:
            if num>N:
                record[N]+=1
            else:
                record[num]+=1
        larger = 0
        for re in range(N, 0, -1):
            larger = larger+record[re]
            if larger == re:
                return re
        return -1
        