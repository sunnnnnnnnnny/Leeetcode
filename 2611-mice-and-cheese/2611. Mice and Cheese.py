class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # greedy since first mice need exactly k cheesse
        # should choose the top k cheese where rewrad1[i]>reward2[i]
        # then if not enough, choose the rest top reward1, with pority queue
        # time: O(nLogn) space:O(n)
        n = len(reward1)
        # sort by the difference of 1-2, then we can get the max points
        # as to select the first k of it
        diffOneVsTwo = [(reward1[i]-reward2[i], reward1[i], reward2[i]) for i in range(n)]
        diffOneVsTwo.sort(reverse=True, key = lambda x:x[0])
        ret = 0
        for i in range(k):
            ret += diffOneVsTwo[i][1]
        
        for i in range(k,n):
            ret += diffOneVsTwo[i][2]
        return ret