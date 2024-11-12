class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # bucket sort with each bucket of contain range valueDiff
        # where each bucket would only have one element, otherwise we find a duplicate
        # time:O(N) space:O(min(N, K))
        minN = min(nums)
        bucketSize = valueDiff+1
        def getId(num):
            nonlocal bucketSize, minN
            
            return (num-minN)//bucketSize
        bucket = defaultdict(list)
        for i, n in enumerate(nums):
            id = getId(n)
            if id in bucket:
                oldN, oldIdx = bucket[id][0]
                if i-oldIdx<=indexDiff:
                    return True
                bucket[id].pop()
            if id-1 in bucket:
                oldN, oldIdx = bucket[id-1][0]
                if n-oldN<=valueDiff and i-oldIdx<=indexDiff:
                    return True
            if id+1 in bucket:
                oldN, oldIdx = bucket[id+1][0]
                if oldN-n<=valueDiff and i-oldIdx<=indexDiff:
                    return True
            bucket[id].append([n, i])
        return False
