class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        # try all permutation with choosing d1 and d2
        # time:O(2^10) as the max signed 32bit int is 2,147,483,647
        # space:O(2)= O(1)
        mi = min(digit1, digit2)
        mx = max(digit1, digit2)
        qu = [mi, mx] if mi!=mx else [mi]
        while qu:
            now = qu.pop(0)
            if now==0 or now>2**31 - 1:
                continue
            if now>k and now%k == 0:
                return now
            qu.append(now*10+mi)
            if mi!=mx:
                qu.append(now*10+mx)
        return -1