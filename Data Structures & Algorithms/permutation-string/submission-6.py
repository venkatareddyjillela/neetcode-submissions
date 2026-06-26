class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for i in range(len(s1)):
            map1[s1[i]] += 1
            map2[s2[i]] += 1

        def find_match():
            for key, val in map1.items():
                if map2[key] != val:
                    return False
            return True

        l, r = 0, len(s1)
        while r < len(s2):
            if find_match():
                return True
            map2[s2[l]] -= 1
            map2[s2[r]] += 1
            
            l += 1
            r += 1

        return find_match()
        

