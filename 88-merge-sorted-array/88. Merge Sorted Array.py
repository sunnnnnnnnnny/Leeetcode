class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # go from the end, comparing and put down the num in num1
        n1Idx = m-1
        n2Idx= n-1
        for i in range(len(nums1)-1, -1, -1):
            now = 0
            if n1Idx>=0 and n2Idx>=0:
                if nums1[n1Idx]>=nums2[n2Idx]:
                    now = nums1[n1Idx]
                    n1Idx -= 1
                else:
                    now = nums2[n2Idx]
                    n2Idx -= 1
            elif n2Idx>=0:
                now = nums2[n2Idx]
                n2Idx -= 1
            else:
                break
            nums1[i] = now
        