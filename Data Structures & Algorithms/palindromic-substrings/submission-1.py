class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            count += self.countPali(s, i, i)
            count += self.countPali(s, i, i+1)

        return count

    def countPali(self, s, l, r):
        count = 0
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count