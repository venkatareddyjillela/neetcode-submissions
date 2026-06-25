class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for par in s:
            if par in hash_map:
                if not stack or stack[-1] != hash_map[par]:
                    return False
                stack.pop()
            else:
                stack.append(par)
        
        return not stack
            