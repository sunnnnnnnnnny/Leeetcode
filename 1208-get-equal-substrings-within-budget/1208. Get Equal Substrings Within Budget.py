class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # By sliding window, to record the cost of each location
        # not greedy, cause its substring, need to connect
        # greedy getting each char cost
        # always select the smallest cost until reaches maxCost
        # time: O(2N) space: O(N)
        N = len(s)
        # costTable = [0]*N
        # for idx in range(len(s)):
        #     cost = ord(s[idx])-ord(t[idx])
        #     if ord(t[idx])>ord(s[idx]):
        #         cost = ord(t[idx])-ord(s[idx])
        #     costTable[idx]=cost
        # getting each cost
        maxLen = 0
        # print(costTable)
        left = 0
        curCost = 0
        # with calculate the cost on the fly, time: O(N) space:O(1)
        for i in range(N):
            # take each i as the end location and try to find the start
            # curCost += costTable[i]
            curCost += abs(ord(s[i])-ord(t[i]))
            while curCost > maxCost:
                # curCost -= costTable[left]
                curCost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            maxLen = max(maxLen, i-left+1)

        return maxLen
        