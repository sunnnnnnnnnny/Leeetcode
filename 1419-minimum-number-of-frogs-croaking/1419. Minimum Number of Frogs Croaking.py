class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # since it needs to finish the first croak then to start a new one
        # so we want to be greedy giving the frog to croak asap
        # record the next char each frog will start
        # at the end validate the left needed ones
        # using a map to record the current char of a frog cnt
        # time:O(N+5) space:O(5) = O(1)
        frogChar = {"c":0, "r":1, "o":2, "a":3, "k":4}
        frogCarr = [0]*len("croak")
        for i in range(len(croakOfFrogs)):
            k = croakOfFrogs[i]
            idx = frogChar[k]
            # only c can add one
            if idx == 0:
                if frogCarr[4]>0:
                    frogCarr[4] -=1
            else:
                if frogCarr[idx-1]<=0:
                    return -1
                frogCarr[idx-1]-=1
            frogCarr[idx] += 1
        for i in range(len(frogCarr)-1):
            if frogCarr[i]>0:
                return -1
        return frogCarr[4]