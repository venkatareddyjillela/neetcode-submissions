class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_oper = ['*', '-', '+', '/']
        stack = []
        for token in tokens:
            if token not in valid_oper:
                stack.append(token)
            else:
                first = float(stack.pop())
                second = float(stack.pop())
                res = 0
                if token == '+':
                    res = second + first
                elif token == '-':
                    res = second - first
                elif token == '*':
                    res = second * first
                else:
                    res = int(second / first)
                stack.append(res)
        return int(stack[0])