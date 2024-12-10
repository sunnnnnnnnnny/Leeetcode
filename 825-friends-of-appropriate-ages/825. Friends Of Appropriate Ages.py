class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # with counting the freq of ages
        # we can directly do the math, and since the time is limited to [0,120]
        # time:O(120^120) = O(1)
        # space:O(120) = O(1)
        def requestAllow(a,b):
            return not(b<=0.5*a+7 or b>a)
        allAges = collections.Counter(ages)
        ret = 0
        for ageA, cntA in allAges.items():
            for ageB, cntB in allAges.items():
                if requestAllow(ageA, ageB):
                    ret += (cntA*cntB)
                    if ageA == ageB:
                        ret -= cntA
        return ret




        # mutual friend is both sending, thus based on the requirement
        # age[y] > age[x]
        # age[y] > 100 && age[x] < 100
        # any age[y]>age[x] will not be friend, thus meaning age is same may be friend
        # sort the age and check the unique age fits the age[y] <= 0.5 * age[x] + 7
        # going from the largest num, check max(half age+7 or age>100) if age y>100
        # time:O(NlogN) space:O(1)
        # ages.sort()
        # hundredLoc = bisect.bisect_left(ages, 100)
        # agesS = len(ages)
        # ret = 0
        # print(ages)
        # for i in range(len(ages)-1, -1, -1):
        #     minAgeFriend = (ages[i])/2+7
        #     smallIdx = bisect.bisect_right(ages, minAgeFriend)
        #     if ages[smallIdx]==minAgeFriend:
        #         smallIdx+=1
        #     if i>smallIdx:
        #         ret += i-smallIdx
        #     print(i,ages[i],minAgeFriend, smallIdx)
        #     sameAge = bisect.bisect_right(ages, ages[i])
        #     if sameAge<=agesS and ages[sameAge-1] == ages[i] and sameAge-1>i:
        #         print(i, ages[i], sameAge)
        #         ret += sameAge-1-i
        # return ret