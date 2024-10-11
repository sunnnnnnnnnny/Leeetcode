class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # intuitive way is to simulate the array of updates
        # time: O(M*length) space:O(length)
        # start from checking all the index in updates, same time as above
        # 3. range catching, make the record on the start and end idx
        # startIdx+inc endIdx+1-inc
        # time:O(M+N) space:O(N)
        ret = [0 for _ in range(length)]
        for u in updates:
            startIdx, endIdx, inc = u
            ret[startIdx]+=inc
            if endIdx+1<length:
                ret[endIdx+1] -= inc
        
        for i in range(1, length):
            ret[i] += ret[i-1]
        return ret