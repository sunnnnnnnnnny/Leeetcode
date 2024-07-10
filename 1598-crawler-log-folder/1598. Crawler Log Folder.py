class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # get the level distance from the main folder after operation
        # using queue to store the current folder
        # time:O(N) space:O(N) queue size is at most len of logs
        folderQ = []
        for log in logs:
            if log == "../":
                if len(folderQ)>0:
                    folderQ.pop()
            else:
                if log != "./":
                    folderQ.append(log)
        return len(folderQ)

        