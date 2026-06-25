class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                new_record = stack[-1] + stack[-2]
                stack.append(new_record)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                new_record = 2 * stack[-1]
                stack.append(new_record)
            else:
                stack.append(int(op))
        
        return sum(stack)