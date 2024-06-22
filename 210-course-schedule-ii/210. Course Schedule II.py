class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        ans = []
        while nextCourse:
            takeCourse = nextCourse.pop()
            ans.append(takeCourse)
            # release other course from prerequsites
            if takeCourse in course2Next.keys():
                for nextCourseId in course2Next[takeCourse]:
                    preCourseCnt[nextCourseId]-=1
                    if preCourseCnt[nextCourseId] == 0:
                        nextCourse.append(nextCourseId)
        return ans if len(ans) == numCourses else []