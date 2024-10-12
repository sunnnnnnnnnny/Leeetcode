class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # traverse from the left to right, with recording only the height when it's increasing 
        # record the height and it's seeing people with prority queue
        # pop until the vision is blocked, and record it back
        # time:O(NlogN) space:O(N), no need of prority qque
        # using stack as the implement, time:O(N) space:O(N)
        n = len(heights)
        ret = [0 for i in range(n)]
        heightQ = []
        # heapq.heappush(heightQ, heights[n-1])
        heightQ.append(heights[n-1])
        for i in range(n-2,-1,-1):
            nowView = 0
            while heightQ:
                prevH = heightQ[-1]
                if prevH<=heights[i]:
                    nowView+=1
                    # heapq.heappop(heightQ)
                    heightQ.pop()
                else:
                    nowView+=1
                    break
            # heapq.heappush(heightQ, heights[i])
            heightQ.append(heights[i])
            ret[i] = nowView
        return ret