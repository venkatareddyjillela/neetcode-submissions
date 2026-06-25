class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue
            second, first = stack.pop(), stack.pop()

            if token == '+':
                res = first + second
            elif token == '-':
                res = first - second
            elif token == '*':
                res = first * second
            else:
                res = int(first / second)
            
            stack.append(res)
        
        return stack[0]
