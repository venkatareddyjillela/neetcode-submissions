class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for ch in s:
            if ch in par_map.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != par_map[ch]:
                    return False
                stack.pop()
        return not stack