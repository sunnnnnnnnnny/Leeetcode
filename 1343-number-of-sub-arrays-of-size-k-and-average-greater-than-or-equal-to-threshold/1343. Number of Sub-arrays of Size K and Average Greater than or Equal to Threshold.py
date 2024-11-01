class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # sliding the subarray of size K, count the sum
        # while the avg is sum/k, if avg>threshold, then ret +=1
        # time: O(N) space:O(1)
        curSum = 0
        ret = 0
        for i in range(len(arr)):
            curSum += arr[i]
            if i>=k-1:
                if i-k>=0:
                    curSum -= arr[i-k]
                avg = curSum//k
                if avg >= threshold:
                    ret += 1
        return ret

