class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # by dfs traversal we can explore all the  connected nodes
        # count the not connected ones
        # time:O(N+M) space:O(N+M)
        adjList = [[]for i in range(n)]
        for e in edges:
            a,b = e
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()
        def dfs(now):
            nonlocal visited
            if now in visited:
                return
            visited.add(now)
            for neighbor in adjList[now]:
                if neighbor not in visited:
                    dfs(neighbor)
            return
        connectComp = 0
        for i in range(n):
            if i not in visited:
                connectComp +=1
                dfs(i)
        return connectComp