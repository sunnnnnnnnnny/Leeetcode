class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         take as original diaskjra
#   the k is the source to all other dist
#  time:O(E*VlogV) space:O(V)
        visited = [-1]*(n+1)
        link = {}
        for edge in times:
            s, t, w = edge
            if s not in link.keys():
                link[s] = []
            link[s].append((t,w))
        nextV = [(0,k)]
        maxDest = 0
        while nextV:
            nowCost, nowIdx = heapq.heappop(nextV)
            if visited[nowIdx]!=-1:
                continue
            visited[nowIdx]=1
            maxDest = max(maxDest, nowCost)
            if nowIdx in link.keys():
                for neighbor in link[nowIdx]:
                    heapq.heappush(nextV, (nowCost+neighbor[1], neighbor[0]))
        for i in range(1,n+1):
            if visited[i] == -1:
                return -1
        return maxDest
        