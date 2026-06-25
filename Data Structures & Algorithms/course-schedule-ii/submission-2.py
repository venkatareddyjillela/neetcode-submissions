class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        output = []
        visit, cycle = set(), set()

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return output