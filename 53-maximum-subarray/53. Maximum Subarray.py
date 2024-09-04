class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp sytle, need only taking care of the positive sum, 
        # when every subarray become <0, then we would start the sum of subarray
        # time:O(n) space:O(1)
        curSum = maxSum = nums[0]
        for n in nums[1:]:
            # compare n and curSum+n is to keep the positive sum of subarray
            # only if n>curSum+n shoudl we reset the array
            curSum = max(n, curSum+n)
            maxSum = max(maxSum, curSum)
        return maxSum








        # # going through the array while the sum til this loc will be
        # # curSum - minSum from all previous nodes
        # # thus getting the max sum for current loc
        # # where the minSum is keep tracked by minHeap
        # # Getting the Sum on the fly
        # # time: O(NLogN)
        # # space: O(N) sumArray with minHeap
        # # curSum = nums[0]
        # # minHeap = []
        # # maxSum = nums[0]
        # # heapq.heappush(minHeap, 0)
        # # heapq.heappush(minHeap, curSum)
        # # for i in range(1, len(nums), 1):
        # #     curSum += nums[i]
        # #     maxCurSum = curSum - minHeap[0]
        # #     maxSum = max(maxSum, maxCurSum)
        # #     heapq.heappush(minHeap, curSum)
        # # return maxSum

        # # By only keeping the connected positive which is greedy
        # # thus we keep record of the cur_subarray or cur
        # # time:O(N) space:O(1)
        # curSub = maxSub = nums[0]
        # for num in nums[1:]:
        #     curSub = max(num, curSub+num)
        #     maxSub = max(maxSub, curSub)
        # return maxSub

        