class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # keep track of the current smallest valid distence and it's index
        # update it as we traverse all the points
        # time: O(N) space:O(1)
        clostestDist = 0
        pointIdx = -1
        for i in range(len(points)):
            xCord, yCord = points[i]
            if x==xCord or y==yCord:
                dist = abs(x-xCord)+abs(y-yCord)
                if pointIdx == -1 or clostestDist>dist:
                    clostestDist=dist
                    pointIdx = i
        return pointIdx