class SnapshotArray:
# brute force of having the space to remember the snapshot of each snap_id
# time:O(1) space:O(snap*n)
# record the base and current
# having the snap only to record the difference from last time 
# while getting the index, we go through each snap and get the latest data
# time:O(snap) space:O(snap*n) worst but can be O(N) 
    def __init__(self, length: int):
        self.len = length
        self.arr = [[] for _ in range(length)]
        self.snapCnt = 0
        # self.snapID2Mod = [{}]

    def set(self, index: int, val: int) -> None:
        if len(self.arr[index])>0:
            lastSnap = self.arr[index][-1][0]
            if lastSnap == self.snapCnt:
                self.arr[index][-1][1] = val
            else:
                self.arr[index].append([self.snapCnt, val])
        else:
            self.arr[index].append([self.snapCnt, val])
        
        # self.snapID2Mod[self.snapCnt][index] = val 
        # print(self.snapCnt, self.snapID2Mod[self.snapCnt])

    def snap(self) -> int:
        self.snapCnt+=1
        # self.snapID2Mod.append({})
        return self.snapCnt-1
        
    def get(self, index: int, snap_id: int) -> int:
        if snap_id>=self.snapCnt:
            return 0
        # for i in range(snap_id,-1,-1):
        #     if index in self.snapID2Mod[i].keys():
        #         return self.snapID2Mod[i][index]
        def binarySearch(indexArr, snap_id):
            l = 0 
            r = len(indexArr)-1
            while l<=r:
                mid = (l+r)//2
                if indexArr[mid][0]==snap_id:
                    return mid
                if indexArr[mid][0]<snap_id:
                    l = mid+1
                else:
                    r = mid-1
            return r
        idx = binarySearch(self.arr[index], snap_id)
        # print(self.arr[index], snap_id, idx)
        return self.arr[index][idx][1] if idx>=0 else 0
        # return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)