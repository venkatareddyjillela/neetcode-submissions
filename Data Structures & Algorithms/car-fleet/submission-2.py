class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp = [(position[i], speed[i]) for i in range(len(speed))]

        pos_sp = sorted(pos_sp, key = lambda kv: kv[0], reverse=True)
        time_taken = []
        for p, s in pos_sp:
            time_taken.append((target - p)/s)
        i = 0
        res = []
        while i < len(time_taken):
            if not res:
                res.append(time_taken[i])
            
            if res[-1] > time_taken[i] or res[-1] == time_taken[i]:
                i += 1
                continue

            res.append(time_taken[i])
            i += 1
        return len(res)
            