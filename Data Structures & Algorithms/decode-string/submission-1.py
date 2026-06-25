class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch != ']':
                stack.append(ch)
                continue
            
            curr = ''
            while stack and stack[-1] != '[':
                curr = stack.pop() + curr

            stack.pop()

            num = ''
            while stack and stack[-1].isnumeric():
                num = stack.pop() + num
            
            val = int(num) * curr

            stack.append(val)
        
        return ''.join(stack)




