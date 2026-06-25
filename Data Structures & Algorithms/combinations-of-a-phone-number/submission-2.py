class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
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

        def dfs(i, substring):
            if i >= len(digits):
                res.append(substring)
                return
            
            for j in digitToChar[digits[i]]:
                dfs(i+1, substring+j)
            
            return
        
        dfs(0, '')
        return res
            