class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the course should be taken from the ones without prerequisites
        # we need to calculate the prerequistes list for each course
        # course to prerequisites count
        # mapping of prerequisites
        # course count is N, prerequsites M
        # time: O(M)+O(N) = O(N+M)
        # space: O(2N) course prerequsites count, course to others mapping
        preCourseCnt = [0]*numCourses
        course2Next = {}
        for pre in prerequisites:
            secCourse = pre[0]
            firstCourse = pre[1]
            preCourseCnt[secCourse] += 1
            if firstCourse not in course2Next.keys():
                course2Next[firstCourse] = []
            course2Next[firstCourse].append(secCourse)
        nextCourse = []
        for i in range(numCourses):
            if preCourseCnt[i] == 0:
                nextCourse.append(i)
        courseTakenCnt = 0
        while nextCourse:
            takeCourse = nextCourse.pop()
            courseTakenCnt += 1
            # release other course from prerequsites
            if takeCourse in course2Next.keys():
                for nextCourseId in course2Next[takeCourse]:
                    preCourseCnt[nextCourseId]-=1
                    if preCourseCnt[nextCourseId] == 0:
                        nextCourse.append(nextCourseId)
        return courseTakenCnt == numCourses





        # directed graph
        # If no loop between traversal, then the course can be finished
        # nodeToEdges = {}
        # nodeToParents = {}
        # for preq in prerequisites:
        #     a = preq[0]
        #     b = preq[1]
        #     if a in nodeToEdges:
        #         nodeToEdges[a] += 1
        #     else:
        #         nodeToEdges[a] = 1
        #     if b not in nodeToEdges:
        #         nodeToEdges[b] = 0
        #     if b in nodeToParents:
        #         nodeToParents[b].append(a)
        #     else:
        #         nodeToParents[b] = [a]
        # #  go through the edgeCnt for each outgoing edge is zero
        # #  and remove them from the graph
        # edgeZero = deque()
        # for key in nodeToEdges:
        #     if nodeToEdges[key] == 0:
        #         edgeZero.append(key)
        
        # while len(edgeZero)>0:
        #     levelCnt = len(edgeZero)
        #     for i in range(levelCnt):
        #         removeKey = edgeZero.popleft()
        #         if removeKey in nodeToParents:
        #             for releaseParent in nodeToParents[removeKey]:
        #                 nodeToEdges[releaseParent] -= 1
        #                 if nodeToEdges[releaseParent] == 0:
        #                     edgeZero.append(releaseParent)
        #         del nodeToEdges[removeKey]
        # # if there's still node connect to edge, meaning a loop
        # for key in nodeToEdges:
        #     if nodeToEdges[key] > 0:
        #         return False
        # return True


        
