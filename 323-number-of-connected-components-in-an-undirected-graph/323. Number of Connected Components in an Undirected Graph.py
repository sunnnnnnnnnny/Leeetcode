class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find, then count the node which the root is itself
        # time:O(M+N) space:O(N)
        # build the connection, go through the bfs of each node
        # time:O(M+N) space:O(N*M)
        visited = [0]*n
        connect = defaultdict(set)
        for e in edges:
            a, b = e
            connect[a].add(b)
            connect[b].add(a)
        
        group = 0
        for i in range(n):
            if visited[i]==0:
                group += 1
                visited[i] = 1
                bfsQ = [i]
                while bfsQ:
                    leSize = len(bfsQ)
                    for j in range(leSize):
                        now = bfsQ.pop(0)
                        if now in connect.keys():
                            for nowNext in connect[now]:
                                if visited[nowNext] == 0:
                                    bfsQ.append(nowNext)
                                    visited[nowNext] = 1
        return group
