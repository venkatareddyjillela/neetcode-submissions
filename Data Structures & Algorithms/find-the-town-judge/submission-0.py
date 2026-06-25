class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjMap = defaultdict(list)

        for a, b in trust:
            adjMap[a].append(b)
        
        judges = []
        for i in range(1, n+1):
            if i not in adjMap:
                judges.append(i)
            
        if len(judges) != 1:
            return -1
        judge = judges[0]
        for b in adjMap.values():
            if judge not in b:
                return -1
        
        return judge

            