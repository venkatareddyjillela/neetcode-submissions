class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build adjmap
        adjMap = [[] for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adjMap[crs].append(pre)

        prereqMap = {}
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adjMap[crs]:
                    dep = dfs(pre)
                    for d in dep:
                        prereqMap[crs].add(d)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])

        return res
