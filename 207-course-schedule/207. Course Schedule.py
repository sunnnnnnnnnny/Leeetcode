class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # directed graph
        # If no loop between traversal, then the course can be finished
        nodeToEdges = {}
        nodeToParents = {}
        for preq in prerequisites:
            a = preq[0]
            b = preq[1]
            if a in nodeToEdges:
                nodeToEdges[a] += 1
            else:
                nodeToEdges[a] = 1
            if b not in nodeToEdges:
                nodeToEdges[b] = 0
            if b in nodeToParents:
                nodeToParents[b].append(a)
            else:
                nodeToParents[b] = [a]
        #  go through the edgeCnt for each outgoing edge is zero
        #  and remove them from the graph
        edgeZero = deque()
        for key in nodeToEdges:
            if nodeToEdges[key] == 0:
                edgeZero.append(key)
        
        while len(edgeZero)>0:
            levelCnt = len(edgeZero)
            for i in range(levelCnt):
                removeKey = edgeZero.popleft()
                if removeKey in nodeToParents:
                    for releaseParent in nodeToParents[removeKey]:
                        nodeToEdges[releaseParent] -= 1
                        if nodeToEdges[releaseParent] == 0:
                            edgeZero.append(releaseParent)
                del nodeToEdges[removeKey]
        # if there's still node connect to edge, meaning a loop
        for key in nodeToEdges:
            if nodeToEdges[key] > 0:
                return False
        return True


        
