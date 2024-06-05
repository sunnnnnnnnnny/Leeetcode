class Solution:
    def totalStrength(self, A: List[int]) -> int:
        # brute force could use sliding window for all possible window
        # time: O(N*(N-1)/2) = O(N*N)
        # space: O(N)
        # prefix sum + monostack
        # calculate the prefix sum of each idex => O(N)
        # record the index range of each min numbers => O(N)
        # calculate the above will take O(N)
        # space:O(2N) = O(N)
        mod = 10 ** 9 + 7
        n = len(A)
        
        # print(A)
        # next small on the right
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left
        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                left[stack.pop()] = i
            stack.append(i)
        # print('r then l')
        # print(right)
        # print(left)
        # for each A[i] as minimum, calculate sum
        res = 0
        acc = list(accumulate(accumulate(A), initial = 0))
        # print(acc)
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            # addWill = A[i] * (racc * ln - lacc * rn)
            # # print('idx: ', i, lacc, racc, ln, rn)
            # # print('addWill: ', addWill)
            # res += addWill
            res += A[i] * (racc * ln - lacc * rn) 
            res %= mod
        return res
        