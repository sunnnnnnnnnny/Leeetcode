class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx2Val = {}
        for i in range(len(nums)):
            if nums[i]!=0:
                self.idx2Val[i] = nums[i]
        return

    def getVec(self):
        return self.idx2Val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ret = 0
        sec = vec.getVec()
        # print(sec)
        # print(self.idx2Val)
        mul = sec if len(sec.keys())<len(self.idx2Val.keys()) else self.idx2Val
        other = sec if len(sec.keys())>=len(self.idx2Val.keys()) else self.idx2Val
        # print(mul)
        # print(other)
        for key,val in mul.items():
            if key in other.keys():
                ret += val*other[key]
        return ret


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)