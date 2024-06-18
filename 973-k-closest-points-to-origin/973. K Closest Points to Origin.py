class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate the distance of points to origin, and keep the top k with maxHeap
        # only keep the top k items
        # time: O(NlogK) as traverse the N points, with logK inserts
        # space:O(K) for max heap
        minK = []
        def calDis(x, y):
            return (x*x)+(y*y)
        for i in range(len(points)):
            dis = calDis(points[i][0], points[i][1])
            if i<k:
                heapq.heappush(minK, (-dis, i))
            else:
                # print(-minK[0][0])
                if -minK[0][0]>dis:
                    heapq.heappop(minK)
                    heapq.heappush(minK, (-dis, i))
        ans = []
        while minK:
            item = heapq.heappop(minK)
            ans.append(points[item[1]])
        return ans

        