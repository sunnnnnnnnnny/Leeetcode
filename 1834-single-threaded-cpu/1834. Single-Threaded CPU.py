class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # since we select the shorest time task at each available
        # we sort the task as enqueTime, then as time gpes by we keep sorted by the
        # processing time
        # time: O(nlogn+n) space:O(N)
        n = len(tasks)
        taskSort = [[tasks[i][0],i] for i in range(len(tasks))]
        taskSort.sort(key = lambda x:x[0])
        # should start at the first possible task time
        timeNow = taskSort[0][0]
        ret = []
        waitingTask = []
        taskIdx = 0
        def addTask2Queue(i, timeNow):
            nonlocal n, taskSort, waitingTask, tasks
            while i<n and taskSort[i][0]<=timeNow:
                oriIdx = taskSort[i][1]
                insertIdx = bisect.bisect_right(waitingTask, (tasks[oriIdx][1],oriIdx))
                waitingTask.insert(insertIdx,(tasks[oriIdx][1],oriIdx))
                i+=1
            return i
        
        while waitingTask or taskIdx<n:
            taskIdx = addTask2Queue(taskIdx, timeNow)
            if len(waitingTask)==0:
                # should jump to the next possible time task
                timeNow=taskSort[taskIdx][0]
                continue
            performTask = waitingTask.pop(0)
            timeNow += performTask[0]
            ret.append(performTask[1])
        return ret



        

        