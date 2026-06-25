class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        if not digits:
            return res

        def dfs(i, curr):
            if i == len(digits):
                res.append(''.join(curr.copy()))
                return

            chars = digit_map[digits[i]]
            for j in range(len(chars)):
                curr.append(chars[j])
                dfs(i+1, curr)
                curr.pop()

            return
        
        dfs(0, [])
        return res


