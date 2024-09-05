class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n^2 time
        # method 1 using the 2 pointer to get the target sum, first sort the array
        # by fixed the first num, the get the sum by l&r pointer
        # for deduplication, the fixed one should skpped the appeared one
        # time: O(nlogn+n*(n)) the inner n is for l&r to get the traverse
        # space:o(1)
        nums.sort()
        ret = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            fix = nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                if fix == -(nums[left]+nums[right]):
                    if left==i+1 or nums[left]!=nums[left-1]:
                        ret.append([fix, nums[left], nums[right]])
                    left+=1
                    right-=1
                elif -fix < nums[left]+nums[right]:
                    right -=1
                else:
                    left+=1
        return ret













        # # count the num to freq, using 2 pointers to get the 2nd 3rd number
        # # time: O(N+N^2) space: O(N)
        # # sort the array, using the 2 pointers, 
        # # time: O(NlogN)+O(N^2)
        # # building hashMap, fixed the 1st number, then go through the hash
        # # time:O(N) for building hash, O(N^2)
        # # space:O(N) 
        # # ans = []
        # # n = len(nums)
        # # def twoSum(firstIdx, n):
        # #     nonlocal ans
        # #     seen = set()
        # #     secondIdx = firstIdx+1
        # #     while secondIdx<n:
        # #         target = -(nums[firstIdx]+nums[secondIdx])
        # #         if target in seen:
        # #             ans.append([nums[firstIdx], nums[secondIdx], target])
        # #             while secondIdx+1<n and nums[secondIdx] == nums[secondIdx+1]:
        # #                 secondIdx += 1
        # #         seen.add(nums[secondIdx])
        # #         secondIdx+=1
        # # nums.sort()
        # # for i in range(n):
        # #     # as we are sorted, not possible the number of positive can sum up to be zero
        # #     if nums[i]>0:
        # #         break
        # #     if i==0 or nums[i-1] != nums[i]:
        # #         twoSum(i, n)
        # # return ans


        # num2Freq = collections.Counter(nums)
        # ans = []
        # uniqueN = list(num2Freq.keys())
        # # print(uniqueN)
        # k = len(uniqueN)
        # for i in range(k):
        #     target  = -uniqueN[i]
        #     num2Freq[-target] -= 1
        #     for secondIdx in range(i, k):
        #         second = uniqueN[secondIdx]
        #         if num2Freq[second]  == 0:
        #             continue
        #         for thirdIdx in range(secondIdx, k):
        #             third = uniqueN[thirdIdx]
        #             if num2Freq[third] == 0:
        #                 continue
        #             elif secondIdx == thirdIdx and num2Freq[third] ==1:
        #                 continue
        #             if second+third == target:
        #                 ans.append([uniqueN[i], second, third])
        #     num2Freq[-target] += 1
        # return ans


        # # count the num to freq
        # # fixed the 3rd num and go through the num list to see if getting the set
        # # time: O(N)+O(K*K)
        # # space:O(N)
        # # num2Freq = collections.Counter(nums)
        # # ans = set()
        # # for n in num2Freq.keys():
        # #     target = -n
        # #     for m in num2Freq.keys():
        # #         if num2Freq[m]==1:
        # #             continue
        # #         need = target-m
        # #         if need in num2Freq.keys():
        # #             ans.add([n, m, need])
        # # return ans
        