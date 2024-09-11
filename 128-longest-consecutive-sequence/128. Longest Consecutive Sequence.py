
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # direct sorting is O(NlogN+N) time
        # put the n as key to locate them fast
        # by only checking the start of possible continue array
        # we would atmost check the array twice: time: O(N) space:O(n) for set
        numSet = set(nums)
        ret = 0
        for n in nums:
            # to get the head of the continue array
            if n-1 not in numSet:
                curN = n
                curStreak = 1
                while curN+1 in numSet:
                    curN +=1
                    curStreak += 1
                ret = max(ret, curStreak)
        return ret
            
            



