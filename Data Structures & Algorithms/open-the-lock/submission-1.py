class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        if '0000' == target:
            return 0

        visit = set(deadends)

        if target in visit:
            return -1
        
        q = deque(['0000'])
        level = 0

        while q:
            level += 1
            for _ in range(len(q)):
                lock = q.popleft()

                for i in range(4):
                    options = str((int(lock[i]) + 1) % 10), str((int(lock[i])-1 + 10) % 10)
                    for option in options:
                        nextLock = lock[:i] + option + lock[i+1:]
                                                
                        if nextLock in visit:
                            continue


                        if nextLock == target:
                            return level
                        visit.add(nextLock)
                        q.append(nextLock)
        return -1