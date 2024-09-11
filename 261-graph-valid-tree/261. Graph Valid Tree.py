class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is a non-cycle graph
        # thus by giving the adjacency list, 
        # we use dfs traversal then if we can discover all nodes without cycle=>tree
        # time:O(N), space:O(N+M) M is edges
        # for a graph to be tree, the edge needs to be n-1 and no cycle
        if len(edges)!=n-1:
            return False
        adjList = [[] for i in range(n)]
        for e in edges:
            a, b = e
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()
        def dfs(now, parent, adjList):
            nonlocal visited
            if now in visited:
                return False
            
            visited.add(now)
            for neighbor in adjList[now]:
                if neighbor != parent:
                    if not dfs(neighbor, now, adjList):
                        return False
            return True
        return dfs(0, -1, adjList) and len(visited)==n