class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # count the arrays and go through unique numbers to get the interset
        # time:O(N+M+max(N,M)) space:O(N+M)
        arr1 = collections.Counter(nums1)
        arr2 = collections.Counter(nums2)
        ret = []
        for key,val in arr1.items():
            if key in arr2.keys():
                minFreq = min(val, arr2[key])
                newArr = [key]*minFreq
                ret = ret+ newArr
        return ret
        