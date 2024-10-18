class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # using traverse to get all the empty sit
        # time:O(N) space:O(1)
        zeroCnt = 0
        ret = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                # first time seeing the people
                if ret == -1:
                    ret = zeroCnt
                else:
                    dist = zeroCnt//2+zeroCnt%2
                    ret = max(ret, dist)
                zeroCnt = 0
            else:
                zeroCnt+=1
        if seats[-1] == 0:
            ret = max(ret, zeroCnt)
        return ret
        