class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window to get all the possible odd num of k
        # once we find a nice str, will add one
        # tiem:O(N) space:O(1)
        niceCnt = 0
        left = 0
        right = 0
        oddCnt = 0
        while right<len(nums):
            if nums[right]%2 == 1:
                oddCnt += 1
            # print(left, right, oddCnt)
            while oddCnt>k and left<right:
                if nums[left]%2 == 1:
                    oddCnt -= 1
                left +=1
            
            if oddCnt == k:
                niceCnt += 1
                # print(left, right, niceCnt)
                # try to shrink the left and see if it will still stay nice
                for i in range(left, right+1):
                    if nums[i]%2 == 1:
                        if left!=i:
                            niceCnt += 1
                        break
                    if i==left:
                        continue
                    niceCnt += 1
                    # print(i, right, oddCnt)
                    
            right += 1
        return niceCnt
