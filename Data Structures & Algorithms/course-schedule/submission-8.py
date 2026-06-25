class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep_map = {i: [] for i in range(numCourses)}

        for course, depends in prerequisites:
            dep_map[course].append(depends)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if not dep_map[crs]:
                return True
            visit.add(crs)
            for dep in dep_map[crs]:
                if not dfs(dep):
                    return False
            visit.remove(crs)
            dep_map[crs] = []
            return True
 

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

            

