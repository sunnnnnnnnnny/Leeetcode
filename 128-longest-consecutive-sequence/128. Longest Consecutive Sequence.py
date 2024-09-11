class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not limited to O(N), then sort to count=>O(NlogN+N)
        # iterate the list, using a dict to keep track of the current groups
        # check each num for it's prev and after to merge into the group
        # only keep the boarder of the num in the list
        # above self-idea hard to implement

        # By only taking the start of the iteration to consider
        # look for the combination of connected sequence
        # runtime is O(N) as we only have the start of sequence look after
        # O(N+N), with set lookup is O(1) for each operation
        allNums = set(nums)
        maxGroupSize = 0
        for num in allNums:
            # take only the start of a sequence
            if num-1 not in allNums:
                currentNum = num
                currentSize = 1
                while currentNum+1 in allNums:
                    currentNum += 1
                    currentSize +=1
                maxGroupSize = max(maxGroupSize, currentSize)

        return maxGroupSize

        