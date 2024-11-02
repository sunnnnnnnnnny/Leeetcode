class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # x-x, y-y is the same as key
        # time:O(N^2) space:O(N)
        if len(points)==1:
            return 1
        ret = 2
        for i in range(len(points)):
            # take each node i as the base, calculate how many same angle nodes
            ratio = {}
            for j in range(len(points)):
                if i!= j:
                    x = points[i][0]-points[j][0]
                    y = points[i][1]-points[j][1]
                    key = math.atan2(x,y)
                    if key in ratio.keys():
                        ratio[key] += 1
                    else:
                        ratio[key] = 1
            ret = max(ret, max(ratio.values())+1)
        return ret