class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # sort the timeslot together , then merge the overlapped ones
        # end only when a slot is found
        # time:O(NlogN+N) space:O(N)
        slots1.sort(key= lambda x:x[0])
        slots2.sort(key= lambda x:x[0])
        i = 0
        j = 0
        while i<len(slots1) and j<len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            overS = max(s1, s2)
            overE = min(e1, e2)
            if overS<overE and overE-overS>=duration:

                return [overS,min(overE, overS+duration)]

            if e1<=e2:
                i+=1
            else:
                j+=1
        return []
