class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # since all child will decrease happiness after each turn
        # thus greedy select the top K value of the happiness child
        # then minus the k-1 turns of decreament: 
        # time: O(N+KlogN) building the max heap O(N) and pop K items with each cost O(logN)
        # space: O(N) of the heap
        # python default is min heap
        maxKItem = [-h for h in happiness]
        heapq.heapify(maxKItem)
        ret = 0
        for i in range(k):
            nowHappy = -heapq.heappop(maxKItem)
            curHappy = nowHappy-i if nowHappy-i>0 else 0
            if curHappy == 0:
                break
            ret += curHappy
        # for idx in range(len(maxKItem)):
        #     nowHappy = maxKItem[idx]-idx if maxKItem[idx]-idx>0 else 0
        #     if nowHappy == 0:
        #         break
        #     ret += nowHappy
        return ret
        