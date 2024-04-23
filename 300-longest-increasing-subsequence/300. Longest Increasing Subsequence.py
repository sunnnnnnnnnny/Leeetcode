class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # the longest sequence is the max(smaller num in front+1)
        # if no smaller the sequence is 1
        # use dict to store the appeared num and it's max sequence len
        # even same number appeared, it need strictly increase we can update it
        appeared_num = {}
        maxLen = 1
        for num in nums:
            max_len_cur = 1
            for ap_num in appeared_num.keys():
                if num<=ap_num:
                    continue
                max_len_cur = max(max_len_cur, appeared_num[ap_num]+1) 
            appeared_num[num] = max(appeared_num[num], max_len_cur) if num in appeared_num else max_len_cur
            maxLen = max(maxLen, appeared_num[num])
        # print(appeared_num)
        return maxLen
                