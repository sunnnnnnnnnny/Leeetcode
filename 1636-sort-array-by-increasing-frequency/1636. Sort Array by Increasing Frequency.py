class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # create the freq to num then first sort by freq increasing 
        # second sort by num decreasing if freq same
        # time: O(NlonN+N) = O(NlogN) space:O(N) for the freq2num
        num2Freq = {}
        maxNum = max(nums)
        for i in nums:
            if i not in num2Freq.keys():
                num2Freq[i] = 0
            num2Freq[i]+=1
        freq2num = [(num2Freq[x],x) for x in num2Freq.keys()]
        # print(freq2num)
        def sort_first_increasing_second_num_increasing(it):
            nonlocal maxNum
            freq = it[0]
            n = it[1]
            # sort original as asending order, 
            # thus the second value in opposite will give decending order
            return (freq, -n)
        freq2num.sort(key = sort_first_increasing_second_num_increasing)
        # print(freq2num)
        ret  = [] 

        for x in freq2num:
            for _ in range(x[0]):
                ret.append(x[1])
        return ret
        
        