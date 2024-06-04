class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use monotonic stack to record the first greater element in nums2
        # build the rightGreater array with stack and dict => O(N)+O(N)
        # go through the nums1 with locating the idx in nums2 => O(M)
        # time: O(M+N+N)=>O(N) space:O(N)
        numsHash = {}
        rightGreater = [-1]*len(nums2)
        rightStack = deque()
        for idx in range(len(nums2)):
            numsHash[nums2[idx]] = idx
            while len(rightStack)>0 and rightStack[-1]<nums2[idx]:
                findGreater = rightStack.pop()
                rightGreater[numsHash[findGreater]] = nums2[idx]
            rightStack.append(nums2[idx])
        ret = [-1]*len(nums1)

        for idx in range(len(nums1)):
            # since num1 is subset of num2, didn't check if it exists
            locNum2 = numsHash[nums1[idx]]
            ret[idx] = rightGreater[locNum2]
        return ret


        