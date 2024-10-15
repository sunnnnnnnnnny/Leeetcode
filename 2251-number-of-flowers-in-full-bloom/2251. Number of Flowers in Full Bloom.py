class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # sort flowers and people with the starttime and time
        # using a pq for flower end time, everytime we have a new people then we pop out the finished flowers, and add new ones
        # time:O(2*NlogN+MlogM) space:O(N)
        bloom = []
        flowers.sort(key = lambda x:x[0])
        people2Idx = [(people[i], i) for i in range(len(people))]
        people2Idx.sort(key = lambda x:x[0])
        # print(people2Idx)
        ret = [0] * len(people)
        flowerIdx = 0
        # print(flowers)
        for i in range(len(people)):
            viewTime = people2Idx[i][0]
            while len(bloom):
                nextCloseFlower = bloom[0]
                if nextCloseFlower<viewTime:
                    heapq.heappop(bloom)
                else:
                    break
            while flowerIdx<len(flowers):
                if flowers[flowerIdx][0]<=viewTime:
                    if flowers[flowerIdx][1]>=viewTime:
                        heapq.heappush(bloom, flowers[flowerIdx][1])
                    flowerIdx+=1
                else:
                    break
            ret[people2Idx[i][1]] = len(bloom)
        return ret