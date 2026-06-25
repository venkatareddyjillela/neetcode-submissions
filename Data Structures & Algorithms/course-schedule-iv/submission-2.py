class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        pre_req_map = {}

        def dfs(crs):
            if crs in pre_req_map:
                return pre_req_map[crs]
            
            pre_req_map[crs] = set()
            for pre in pre_map[crs]:
                for i in dfs(pre):
                    pre_req_map[crs].add(i)
                pre_req_map[crs].add(pre)
            return pre_req_map[crs]

        for i in range(numCourses):
            dfs(i)
        
        print("pre_req_map:", pre_req_map)
        answers = []
        for crs, pre in queries:
            answers.append(True if pre in pre_req_map[crs] else False)
        
        return answers

