class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1List = version1.split('.')
        v2List = version2.split('.')
        v1idx = v2idx = 0
        while v1idx<len(v1List) or v2idx<len(v2List):
            nowV1 = "0"
            if v1idx<len(v1List):
                nowV1 = v1List[v1idx]
                v1idx +=1
            nowV2 = "0"
            if v2idx<len(v2List):
                nowV2 = v2List[v2idx]
                v2idx+=1
            if int(nowV1)>int(nowV2):
                return 1
            elif int(nowV1)<int(nowV2):
                return -1
        return 0

            