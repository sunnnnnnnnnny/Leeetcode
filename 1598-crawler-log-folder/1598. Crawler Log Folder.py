class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # get the level distance from the main folder after operation
        # using stack to store the current folder
        # time:O(N) space:O(N) stack size is at most len of logs
        # or using counter will save the space
        # folderQ = []
        # for log in logs:
        #     if log == "../":
        #         if len(folderQ)>0:
        #             folderQ.pop()
        #     else:
        #         if log != "./":
        #             folderQ.append(log)
        # return len(folderQ)
        levelCnt = 0
        for log in logs:
            if log == "../":
                if levelCnt>0:
                    levelCnt -= 1
            else:
                if log != "./":
                    levelCnt += 1
        return levelCnt

        