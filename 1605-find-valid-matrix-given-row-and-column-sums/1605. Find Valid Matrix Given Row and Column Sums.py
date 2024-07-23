class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # greedy to put the possible ans and leave the rest as zero
        # start from row sum to get the first column, 
        # the intersect is (i,j)  rowSum[i] colSum[j], get the min of intersect
        # and detucted the used number
        # time: O(NM) space:O(NM) for the result
        rowLen = len(rowSum)
        colLen = len(colSum)
        ret = [[0 for _ in range(colLen)] for _ in range(rowLen)]
        # for j in range(colLen):
        #     for i in range(rowLen):
        #         ret[i][j] = min(rowSum[i],colSum[j])
        #         rowSum[i] -= ret[i][j]
        #         colSum[j] -= ret[i][j]
        i,j = 0,0
        # could save more time on only taking care the non-zero elements
        while i<rowLen and j<colLen:
            ret[i][j] = min(rowSum[i],colSum[j])
            rowSum[i] -= ret[i][j]
            colSum[j] -= ret[i][j]
            if rowSum[i] == 0:
                i+=1
            else:
                j+=1

        return ret
        