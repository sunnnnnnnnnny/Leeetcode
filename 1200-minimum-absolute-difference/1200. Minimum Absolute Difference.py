class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort them with asending order, then check the min diff
        # time:O(nlogn) space:O(n)
        arr.sort()
        minDiff = arr[-1]-arr[0]
        ret = []
        for i in range(1, len(arr)):
            nowDiff = arr[i]-arr[i-1]
            if nowDiff<minDiff:
                minDiff = nowDiff
                ret = [[arr[i-1], arr[i]]]
            elif nowDiff == minDiff:
                ret.append([arr[i-1], arr[i]])
        return ret