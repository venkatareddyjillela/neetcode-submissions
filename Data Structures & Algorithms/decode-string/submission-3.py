class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ''

        for ch in s:
            if ch == ']':
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()
                stack.append(int(stack.pop()) * curr)
            else:
                if ch.isnumeric() and stack and stack[-1].isnumeric():
                    stack.append(stack.pop() + ch)
                else:
                    stack.append(ch)
                
        return ''.join(stack)
                    
                