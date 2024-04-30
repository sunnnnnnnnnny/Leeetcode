class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree meaning no cycle and no left out node
        # where tree is fully-connected meaning n nodes, n-1 edges
        # using the bfs/dfs to traverse from any node, and if all
        # nodes can be reached, meaning it's fully-connected
        if len(edges) != n-1:return False
        adj_list = [[] for _ in range(n)]
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        queue = deque([0])
        seen = set({0})
        while queue:
            levelCnt = len(queue)
            for i in range(levelCnt):
                now = queue.popleft()
                for neighbor in adj_list[now]:
                    if neighbor in seen:
                        continue
                    queue.append(neighbor)
                    seen.add(neighbor)
        return len(seen) == n

        # Below checks both cycle and if fully-connected => O(N+E)
        # yet if a graph with N-1 edges, even there is cycle we don't care
        # b/c indicating it must have a node left unconnected
        # so to use this, we could ignore the cycle check and focus on traversal
        # then final checking if all node is linked => O(N+E) = O(N+N) = O(N)
        # # seen to detect if cycle appeared
        # seen = set()
        # def dfs(node, parent):
        #     if node in seen:
        #         return;
        #     seen.add(node)
        #     for neighbor in adj_list[node]:
        #         if neighbor == parent:
        #             continue
        #         if neighbor in seen:
        #             return False
        #         result = dfs(neighbor, node)
        #         if not result: return False
        #     return True
        # # checking if no cycle and all node can be reached
        # return dfs(0,-1) and len(seen) == n