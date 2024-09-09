class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # calculate the inComing degree of each course(node)
        # by removing the inComing degree=0 node, we can reduce the queue
        # if the queue is empty then all cource can be taken
        # assume no duplicate edge, and all prerequisites are in 0-n-1
        # time: O(p+n) space:O(n)
        inComing = [0 for _ in range(numCourses)]
        preCourse = {}
        for prep in prerequisites:
            a, b = prep
            inComing[b]+=1
            if a not in preCourse.keys():
                preCourse[a] = []
            preCourse[a].append(b) 
        takeCourses = []
        for i in range(numCourses):
            if inComing[i] == 0:
                takeCourses.append(i)
        courseCnt = 0
        while takeCourses:
            now = takeCourses.pop(0)
            courseCnt += 1
            if now in preCourse.keys():
                for nextCourse in preCourse[now]:
                    inComing[nextCourse]-=1
                    if inComing[nextCourse] == 0:
                        takeCourses.append(nextCourse)
        return True if courseCnt == numCourses else False