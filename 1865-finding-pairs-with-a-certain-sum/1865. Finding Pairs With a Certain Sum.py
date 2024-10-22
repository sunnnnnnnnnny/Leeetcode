class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # ini the num having and count their sum
        # time:O(N^2) space:O(M)
        self.nums1 = nums1
        self.nums2 = nums2
        self.twoCnt = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        # update the sum time:O(1)
        oriN2 = self.nums2[index]
        self.nums2[index] += val
        self.twoCnt[oriN2] -= 1
        self.twoCnt[self.nums2[index]]+=1
        

    def count(self, tot: int) -> int:
        ret = 0
        for i in range(len(self.nums1)):
            left = tot-self.nums1[i]
            if left in self.twoCnt.keys():
                ret += self.twoCnt[left]
        return ret
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)