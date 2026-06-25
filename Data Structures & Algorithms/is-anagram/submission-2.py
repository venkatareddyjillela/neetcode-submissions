class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        stack = [0] * 26
        for ch in s:
            stack[ord(ch) - ord('a')] += 1
        
        for ch in t:
            stack[ord(ch) - ord('a')] -= 1
            if stack[ord(ch) - ord('a')] < 0:
                return False
        return True
            