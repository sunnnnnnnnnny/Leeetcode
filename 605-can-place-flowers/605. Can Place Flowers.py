class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # calculate the consecutive 0's, then for each consecutive 0
        # we can plant (x-1)//2 flowers if the edge are 1, front and tail
        # can get (x-1)//2+1
        # time:O(N) space:O(1)
        consZero = 0
        prev = -1
        ret = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i==0:
                    prev = i
                    ret += 1
                else:
                    if flowerbed[i-1]==0 and prev != i-1:
                        prev = i
                        ret += 1
            else:
                if i>0 and flowerbed[i-1]==0 and prev == i-1:
                    ret -= 1
                
        # print(ret)
        return True if ret>=n else False
