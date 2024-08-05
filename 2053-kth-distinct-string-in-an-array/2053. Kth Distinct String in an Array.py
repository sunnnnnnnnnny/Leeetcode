class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # creating a map for counting the appearance, then take only the cnt 1
        # time:O(N) space:O(N)
        appear = collections.Counter(arr)
        # idx = 0
        # for key, cnt in appear.items():
        #     if cnt == 1:
        #         idx+=1
        #         if idx == k:
        #             return key
        
        for key in arr:
            if appear[key] == 1:
                k-=1
            if k== 0:
                return key
        return ""

        