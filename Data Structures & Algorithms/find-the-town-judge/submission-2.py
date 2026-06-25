class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inbound = defaultdict(list)
        outbound = defaultdict(list)
        for a, b in trust:
            inbound[b].append(a)
            outbound[a].append(b)
        
        for i in range(1, n+1):
            if not outbound[i] and len(inbound[i]) == n-1:
                return i
        
        return -1