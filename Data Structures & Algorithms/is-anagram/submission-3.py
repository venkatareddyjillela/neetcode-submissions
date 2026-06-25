class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        stack = [0] * 26
        for i in range(len(s)):
            stack[ord(s[i]) - ord('a')] += 1
            stack[ord(t[i]) - ord('a')] -= 1

        for val in stack:
            if val != 0:
                return False
                
        return True
        
        # for ch in t:
        #     stack[ord(ch) - ord('a')] -= 1
        #     if stack[ord(ch) - ord('a')] < 0:
        #         return False
        # return True
            