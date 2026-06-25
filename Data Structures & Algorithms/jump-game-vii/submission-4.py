class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s or s[-1] != '0' or s[0] != '0':
            return False
        n = len(s)
        q = deque([0])
        farthest = 0
        while q:
            i = q.popleft()
            start = max(i+minJump, farthest+1)
            for j in range(start, min(i+maxJump+1, n)):
                if s[j] == '0':
                    q.append(j)
                    if j == n-1:
                        return True
            farthest = i+maxJump
        return False

                