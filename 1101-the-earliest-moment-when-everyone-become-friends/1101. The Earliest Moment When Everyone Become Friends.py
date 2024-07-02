class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # similar to prerequset of classes
        # union find with sort the timestamp by earliest
        # time completxity;O(N*L) L is the log size
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
            if groupSize[xGroup]>=groupSize[yGroup]:
                friendG[yGroup] = xGroup
            else:
                friendG[xGroup] = yGroup
        logs.sort()
        def allAreFriends():
            zeroG = findGroup(0)
            for i in range(1, n):
                nG = findGroup(i)
                if nG != zeroG:
                    return False
            return True
        for log in logs:
            timeL = log[0]
            union(log[1], log[2])
            # check all frined group same
            if allAreFriends():
                return timeL
        return -1