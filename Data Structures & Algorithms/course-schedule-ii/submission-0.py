class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        cycle = set()
        order = []

        def dfs(crs):
            if crs in cycle:
                return []
            if crs in visit:
                return order
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return []

            cycle.remove(crs)
            visit.add(crs)
            order.append(crs)
            return order
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
