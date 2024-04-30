class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # bfs of the nodes not seen, then we can count how many component
        # Time: O(N+E) storage: O(N+E)
        # best way should be union find => more intuitive
        # time: O(N+E*union find time), storage: O(N+N)
        parent = list(range(n))
        rank = [0]*n
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(x, y):
            x, y = find(x), find(y)
            if rank[x]<rank[y]:
                parent[x] = y
            else:
                if rank[x] == rank[y]:
                    parent[y] = x
                    rank[x] += 1
                else:
                    parent[y] = x
        # union by all the connected edges
        for x, y in edges:
            union(x, y)
        # getting all the parent of each node in set, 
        # the count of top parent will be the distinct group
        return len({find(i) for i in range(n)})
        # adj_list = [[] for _ in range(n)]
        # for a, b in edges:
        #     adj_list[a].append(b)
        #     adj_list[b].append(a)
        # seen = set()
        # def dfs(node):
        #     if node in seen:
        #         return
        #     seen.add(node)
        #     for neighbor in adj_list[node]:
        #         if neighbor in seen:
        #             continue
        #         dfs(neighbor)
        # groupCnt = 0
        # for i in range(n):
        #     if i not in seen:
        #         groupCnt+=1
        #     dfs(i)
        # return groupCnt
        
        