class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # make an empty list for every course
        graph = []

        for i in range(numCourses):
            graph.append([])

        # fill the graph
        # [course, prereq] means:
        # course needs prereq first
        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]

            graph[course].append(prereq)

        # courses we are checking RIGHT NOW
        visiting = set()

        def dfs(course):

            # if we come back to a course
            # we are already checking -> cycle
            if course in visiting:
                return False

            # if this course has no prerequisites
            # it is safe
            if len(graph[course]) == 0:
                return True

            # start checking this course
            visiting.add(course)

            # check all courses it needs
            for prereq in graph[course]:

                if dfs(prereq) == False:
                    return False

            # done checking this course
            visiting.remove(course)

            # mark it as safe so we don't check it again
            graph[course] = []

            return True

        # check every course
        for course in range(numCourses):

            if dfs(course) == False:
                return False

        return True