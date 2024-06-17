class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # the gas == gain should be larger than the cost to make it to the next
        # while select the start point should be at positive gain 
        # by intuitive it should be the max positive gain
        # time:O(N) space:O(1)
        # if sum(gas)<sum(cost):
        #     return -1
        curIdx = 0
        curGain = 0
        totalGain = 0
        # changing the curGain <0  as it's not a valid start
        # after going all nodes, check if totalGain is>0 to make sure possible going around
        # the intuition is for i to j failed to pass, then starting in any point btw i~j
        # will failed to pass j, thus no need to examie againg
        for idx in range(0, len(gas), 1):
            curGain += (gas[idx]-cost[idx])
            totalGain += (gas[idx]-cost[idx])
            if curGain<0:
                curGain = 0
                curIdx = idx+1
        return curIdx if totalGain>=0 else -1



        