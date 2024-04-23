class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ### check the distance from start to target
        ### deal one wheel at a time
        ### if the lock is about to be dead, try the other side
        # recursive of bfs
        def getNextNum(curChar, isUp):
            if curChar == "0":
                if isUp:
                    return '1'
                else:
                    return '9'
            elif curChar == "1":
                if isUp:
                    return '2'
                else:
                    return '0'
            elif curChar == "2":
                if isUp:
                    return '3'
                else:
                    return '1'
            elif curChar == "3":
                if isUp:
                    return '4'
                else:
                    return '2'
            elif curChar == "4":
                if isUp:
                    return '5'
                else:
                    return '3'
            elif curChar == "5":
                if isUp:
                    return '6'
                else:
                    return '4'
            elif curChar == "6":
                if isUp:
                    return '7'
                else:
                    return '5'
            elif curChar == "7":
                if isUp:
                    return '8'
                else:
                    return '6'
            elif curChar == "8":
                if isUp:
                    return '9'
                else:
                    return '7'
            elif curChar == "9":
                if isUp:
                    return '0'
                else:
                    return '8'
        self.visited = set()
        # this is dfs
        def cntTurnUpDown(self, edgeCnt, cur, tar, deadSet):
            for i in range(4):
                for j in range(2):
                    dirct = (j==0)
                    nextI = getNextNum(cur[i],dirct)
                    nextState = list(cur)
                    nextState[i] = nextI
                    nextStr = ''.join(nextState)
                    if nextStr == tar:
                        return edgeCnt
                    if nextStr not in self.visited:
                        if nextStr not in deadends:
                            cntTurnUpDown(self, edgeCnt+1, nextStr, tar, deadends)
                            self.visited.add(nextStr)
            return -1
        curState = "0000"
        deadSet = set(deadends)
        # dfs will timeout
        # return cntTurnUpDown(self, 0, curState, target, deadSet)
        # bfs with deque
        if curState in deadSet:
            return -1
        if curState == target:
            return 0
        pendingBfs = deque()
        pendingBfs.append(curState)
        self.visited.add(curState)
        cnt = 0
        while pendingBfs:
            curLevelNodeCnt = len(pendingBfs)
            for _ in range(curLevelNodeCnt):
                cur = pendingBfs.popleft()
                for i in range(4):
                    for j in range(2):
                        dirct = (j==0)
                        nextI = getNextNum(cur[i],dirct)
                        nextState = list(cur)
                        nextState[i] = nextI
                        nextStr = ''.join(nextState)
                        if nextStr == target:
                            return cnt+1
                        if nextStr not in self.visited:
                            if nextStr not in deadends:
                                pendingBfs.append(nextStr)
                                self.visited.add(nextStr)
            cnt += 1
        return -1
                

                

        


            
            