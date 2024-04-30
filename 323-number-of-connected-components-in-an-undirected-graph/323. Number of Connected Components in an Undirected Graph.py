class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # bfs of the nodes not seen, then we can count how many component
        # Time: O(N+E) storage: O(N+E)
        # best way should be union find
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                dfs(neighbor)
        groupCnt = 0
        for i in range(n):
            if i not in seen:
                groupCnt+=1
            dfs(i)
        return groupCnt
        
        