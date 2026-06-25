class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        res = 0
        for i in range(n-1, -1, -1):
            if i < n-1 and roman_int_map[s[i]] < roman_int_map[s[i+1]]:
                res -= roman_int_map[s[i]]
            else:
                res += roman_int_map[s[i]]
        return res