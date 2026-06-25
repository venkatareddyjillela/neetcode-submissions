class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = Counter(s1)
        count2 = defaultdict(int)
        n = len(s2)
        l, r = 0, 0

        while r < n:
            count2[s2[r]] += 1

            while l <= r and (s2[r] not in count1) or (count2[s2[r]] > count1[s2[r]]):
                count2[s2[l]] -= 1
                l += 1
            
            if r-l+1 == len(s1):
                return True
            
            r += 1
        return False

