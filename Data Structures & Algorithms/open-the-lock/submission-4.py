class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        start = '0000'
        if target == start:
            return 0
        
        if target in visit:
            return -1
        
        if start in visit:
            return -1
        visit.add(start)
        q = deque([start])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    up = str((int(lock[i])+1+10) % 10)
                    down = str((int(lock[i])-1+10) % 10)
                    options = [up, down]
                    for option in options:
                        nextLock = lock[:i] + option + lock[i+1:]
                        if nextLock in visit:
                            continue
                        
                        if nextLock == target:
                            return level
                        visit.add(nextLock)
                        q.append(nextLock)
        return -1
                    
