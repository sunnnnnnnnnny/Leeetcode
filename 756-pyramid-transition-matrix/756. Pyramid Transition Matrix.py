class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # dp? to check every path for building the next level
        # time:O(2^len(bottom))
        allDict = defaultdict(list)
        memo = {}
        for al in allowed:
            key = al[:2]
            allDict[key].append(al[2])
        def bk(nowS, idx, level, nextBase):
            nonlocal allDict, memo
            if level == 1:
                return True
            if idx == 0 and nowS in memo:
                return memo[nowS]
            if idx==len(nowS)-1:
                # print(nowS, nextBase, level)
                return bk(nextBase, 0, level-1, "")
            # try to build the next part
            key =  nowS[idx:idx+2]
            # print(level, key)
            ret = False
            if key in allDict:
                for posible in allDict[key]:
                    if bk(nowS, idx+1, level, nextBase+posible):
                        ret = True
                        break
            if idx == 0:
                memo[nowS] = ret
            return ret
        return bk(bottom, 0, len(bottom), "")