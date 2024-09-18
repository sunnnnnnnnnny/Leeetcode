class SnapshotArray:
# brute force of having the space to remember the snapshot of each snap_id
# time:O(1) space:O(snap*n)
# record the base and current
# having the snap only to record the difference from last time 
# while getting the index, we go through each snap and get the latest data
# time:O(snap) space:O(snap*n) worst but can be O(N) 
    def __init__(self, length: int):
        self.len = length
        # self.arr = [0 for _ in range(length)]
        self.snapCnt = 0
        self.snapID2Mod = [{}]

    def set(self, index: int, val: int) -> None:
        # self.arr[index] = val
        self.snapID2Mod[self.snapCnt][index] = val 
        # print(self.snapCnt, self.snapID2Mod[self.snapCnt])

    def snap(self) -> int:
        self.snapCnt+=1
        self.snapID2Mod.append({})
        return self.snapCnt-1
        
    def get(self, index: int, snap_id: int) -> int:
        if snap_id>=self.snapCnt:
            return 0
        for i in range(snap_id,-1,-1):
            if index in self.snapID2Mod[i].keys():
                return self.snapID2Mod[i][index]
        return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)