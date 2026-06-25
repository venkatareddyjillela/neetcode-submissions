class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = defaultdict(int)
        for ch in s:
            hash_map[ch] += 1
        
        for ch in t:
            hash_map[ch] -= 1
            if hash_map[ch] < 0:
                return False
        return True