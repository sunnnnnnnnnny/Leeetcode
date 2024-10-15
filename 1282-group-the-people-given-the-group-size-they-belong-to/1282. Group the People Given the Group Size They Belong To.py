class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # based on the groupsize, we could group people to each parts, then making the calculation of it
        # time:O(N) space:O(N)
        # time:O(NlogN) space:O(1) by sorting we can assign the same user directly
        group2Id = {}
        for i in range(len(groupSizes)):
            key = groupSizes[i]
            if key not in group2Id.keys():
                group2Id[key] = []
            group2Id[key].append(i)
        ret = []
        for key, ids in group2Id.items():
            idx = 0
            while idx<len(ids):
                group = []
                for i in range(idx, idx+key):
                    group.append(ids[i])
                ret.append(group)
                idx += key
        return ret