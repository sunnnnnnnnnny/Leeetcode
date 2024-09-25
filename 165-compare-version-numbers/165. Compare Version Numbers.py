class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # directly go through the both versions
        # time:O(max(N,M)) space:O(max(N,M))
        v1idx = v2idx = 0
        def getNextSperater(now, oriStr):
            retStr = ""
            while now<len(oriStr):
                if oriStr[now] == '.':
                    break
                retStr += oriStr[now]
                now += 1
            return now, retStr
        while v1idx<len(version1) or v2idx<len(version2):
            nowV1 = "0"
            if v1idx<len(version1):
                v1idx, nowV1 = getNextSperater(v1idx, version1)
                v1idx +=1
            nowV2 = "0"
            if v2idx<len(version2):
                v2idx, nowV2 = getNextSperater(v2idx, version2)
                v2idx+=1
            if int(nowV1)>int(nowV2):
                return 1
            elif int(nowV1)<int(nowV2):
                return -1
        return 0
        # # time:O(M+N+max(M,N)), space:O(M+N)
        # v1List = version1.split('.')
        # v2List = version2.split('.')
        # v1idx = v2idx = 0
        # while v1idx<len(v1List) or v2idx<len(v2List):
        #     nowV1 = "0"
        #     if v1idx<len(v1List):
        #         nowV1 = v1List[v1idx]
        #         v1idx +=1
        #     nowV2 = "0"
        #     if v2idx<len(v2List):
        #         nowV2 = v2List[v2idx]
        #         v2idx+=1
        #     if int(nowV1)>int(nowV2):
        #         return 1
        #     elif int(nowV1)<int(nowV2):
        #         return -1
        # return 0

            