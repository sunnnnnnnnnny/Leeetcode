class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # similar to prerequset of classes
        # union find O(N) with sort the timestamp by earliest O(MlogM)
        # union through sorted logs =O(M*a(N))
        # time completxity;O(N+MlogM+M*a(N)) M is the log size
        # space:O(N+M) N for union group, M for sorting
        friendG = [i for i in range(n)]
        groupSize = [1 for i in range(n)]
        def findGroup(x):
            if friendG[x] == x:
                return x
            actualG = findGroup(friendG[x])
            friendG[x] = actualG
            return actualG
        def union(x, y):
            xGroup = findGroup(x)
            yGroup = findGroup(y)
            isMerged = False
            if xGroup == yGroup:
                return isMerged
            isMerged = True
            if groupSize[xGroup]>=groupSize[yGroup]:
                friendG[yGroup] = xGroup
            else:
                friendG[xGroup] = yGroup
            return isMerged
        logs.sort(key = lambda x:x[0])
        groupCnt = n
        # can be replaced by adding a counter at union stage
        def allAreFriends():
            zeroG = findGroup(0)
            for i in range(1, n):
                nG = findGroup(i)
                if nG != zeroG:
                    return False
            return True
        for log in logs:
            timeL = log[0]
            isM = union(log[1], log[2])
            if isM:
                groupCnt -= 1
            if groupCnt == 1:
                return timeL
            # check all frined group same
            # if allAreFriends():
            #     return timeL
        return -1