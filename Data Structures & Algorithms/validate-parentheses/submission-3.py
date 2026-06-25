class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for char in s:
            if char in par_map.values():
                stack.append(char)
            elif not stack or par_map[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack
