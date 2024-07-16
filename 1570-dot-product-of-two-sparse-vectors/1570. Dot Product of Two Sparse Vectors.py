class SparseVector:
    # record the index to val for only non-zero val
    # time:O(N) space:O(N)
    # could also use list((idx,val)) to store the vector
    def __init__(self, nums: List[int]):
        self.idx2Val = {}
        for i in range(len(nums)):
            if nums[i]!=0:
                self.idx2Val[i] = nums[i]
        return

    def getVec(self):
        return self.idx2Val

    # Return the dotProduct of two sparse vectors
    # time:O(min(L1, L2)*O(1) b/c using dictionary of python3
    def dotProduct(self, vec: 'SparseVector') -> int:
        ret = 0
        sec = vec.getVec()
        mul = sec if len(sec.keys())<len(self.idx2Val.keys()) else self.idx2Val
        other = sec if len(sec.keys())>=len(self.idx2Val.keys()) else self.idx2Val
        for key,val in mul.items():
            if key in other.keys():
                ret += val*other[key]
        return ret


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)