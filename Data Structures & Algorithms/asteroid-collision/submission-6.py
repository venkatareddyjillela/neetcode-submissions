class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for v in asteroids:
            while res and v < 0 < res[-1]:
                if abs(v) == res[-1]:
                    res.pop()
                elif abs(v) > res[-1]:
                    res.pop()
                    continue
                break
            else:
                res.append(v)
        return res