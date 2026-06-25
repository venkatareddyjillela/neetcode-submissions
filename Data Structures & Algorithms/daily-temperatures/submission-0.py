class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                val = stack[-1][1]
                result[stack.pop()[1]] = i - val
            stack.append((temperatures[i], i))
        return result