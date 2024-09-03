class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # know when the chalk is used up, 
        # thus need to calculate the prefix sum of the chalk array
        # and caclulate the addidum of the chalk, 
        # once chalk[0]<=k<=sum(chalk[n-1]), do binary search to know which student need to replace
        # time: O(N+logN) or O(2N) if the we calculate twice
        # space:O(N) for the prefix sum
        n = len(chalk)
        prefix = [0]*n
        prefix[0] = chalk[0]
        if prefix[0]>k:
            return 0
        for i in range(1,n):
            prefix[i] = prefix[i-1]+chalk[i]
            if k<prefix[i]:
                return i
        kLeft = k%prefix[-1]
        def binarySearch(preArr,left, right, target):
            while left<right:
                mid = (left+right)//2
                if preArr[mid] <= target:
                    left = mid+1
                else:
                    right = mid
            return right
        t = binarySearch(prefix, 0, n-1, kLeft)
        # print(prefix)
        # print(prefix[-1], n)
        # print(kLeft, t)
        # for i in range(n):
        #     if kLeft<=prefix[i]:
        #         return i
        return t

        