class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # greedy since first mice need exactly k cheesse
        # should choose the top k cheese where rewrad1[i]>reward2[i]
        # then if not enough, choose the rest top reward1, with pority queue
        # time: O(nLogn) space:O(n)
        n = len(reward1)
        reward1More = []
        reward2More = []
        for i in range(n):
            diff = abs(reward1[i]-reward2[i])
            if reward1[i]>reward2[i]:
                heapq.heappush(reward1More, (-diff, i))
            else:
                heapq.heappush(reward2More, (-diff, i))
        leftK = k
        ret = 0
        while reward1More and leftK>0:
            diff, idx = heapq.heappop(reward1More)
            ret += reward1[idx]
            leftK -= 1
        # if the reward1>reward2 doens't fill up the k, then we take the max reward2
        if leftK>0:
            while len(reward2More)>leftK:
                diff, idx = heapq.heappop(reward2More)
                ret += reward2[idx]
            while reward2More:
                diff, idx = heapq.heappop(reward2More)
                ret += reward1[idx]
        # if leftK == 0, the rest should all be eatenn by mice2
        while reward1More:
            diff, idx = heapq.heappop(reward1More)
            ret += reward2[idx]
        while reward2More:
            diff, idx = heapq.heappop(reward2More)
            ret += reward2[idx]
        return ret

