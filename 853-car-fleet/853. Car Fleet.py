class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # brute force actually updating the location of each hour
        # combine the car location as the car fleet
        # time: O(K*N) space:O(N)
        # sorting the car starting pos from end to begging 
        # and get's the time need to arrive target
        # if the time need is < the car before they become the fleet
        # when meeting a car needs more time, then it's the new fleet head
        # time: O(NlogN) space:O(N)
        timeNeed = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        # print(timeNeed)
        ans = cur = 0
        for tUsed in timeNeed[::-1]:
            if tUsed>cur:
                ans+=1
                cur = tUsed
        return ans
        