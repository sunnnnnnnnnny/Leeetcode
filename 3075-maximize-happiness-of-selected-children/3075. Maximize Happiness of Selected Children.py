class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # since all child will decrease happiness after each turn
        # thus greedy select the top K value of the happiness child
        # then minus the k-1 turns of decreament: 
        # time: O(N+K) building the max heap and pop K items
        # space: O(N) of the heap
        maxKItem = heapq.nlargest(k, happiness)
        ret = 0
        for idx in range(len(maxKItem)):
            nowHappy = maxKItem[idx]-idx if maxKItem[idx]-idx>0 else 0
            if nowHappy == 0:
                break
            ret += nowHappy
        return ret
        