class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # dp(i) = max(dp(i-1), book[i]) if same level or dp(i-1)+book[i]
        n = len(books)
        # top-down defining a function f(i,remainingShelfWidth,maxHeight)
        # memo[i][remainingShelfWidth] stores the minimum height of the bookcase 
        # containing all books up to the i-th book with remainingShelfWidth width available on the current shelf.
        memo = [[0 for _ in range(shelfWidth+1)] for _ in range(n)]
        def minHeight(i, remainingShelfWidth, maxHeight):
            nonlocal books, memo, shelfWidth, n
            curBook = books[i]
            maxHeightUpdate = max(maxHeight, curBook[1])
            if i==n-1:
                if remainingShelfWidth>=curBook[0]:
                    return maxHeightUpdate
                return maxHeight+curBook[1]
            if memo[i][remainingShelfWidth]!=0:
                return memo[i][remainingShelfWidth]
            # to the same shelf
            op1Height = maxHeight+minHeight(i+1, shelfWidth-curBook[0], curBook[1])
            if remainingShelfWidth>=curBook[0]:
                op2Height = minHeight(i+1, remainingShelfWidth-curBook[0], maxHeightUpdate)
                memo[i][remainingShelfWidth] = min(op1Height, op2Height)
                return memo[i][remainingShelfWidth]
            memo[i][remainingShelfWidth] = op1Height
            return memo[i][remainingShelfWidth]
        return minHeight(0, shelfWidth, 0)
        # bottom-up dp[i] will store the minimum height of the bookcase containing all
        # books up to and excluding i
        # time:O(N*W) w is the shelfWidth space:O(N)
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = books[0][1]
        for i in range(2, n+1):
            # put in the new shelf
            remainShelfWidth = shelfWidth-books[i-1][0]
            maxHeight = books[i-1][1]
            dp[i] = books[i-1][1]+dp[i-1]
            j = i-1
            while j>0 and remainShelfWidth-books[j-1][0]>=0:
                # trying to put the previous books onto the same shelf
                maxHeight = max(maxHeight, books[j-1][1])
                remainShelfWidth -= books[j-1][0]
                dp[i] = min(dp[i], dp[j-1]+maxHeight)
                j-=1
        return dp[n]

        