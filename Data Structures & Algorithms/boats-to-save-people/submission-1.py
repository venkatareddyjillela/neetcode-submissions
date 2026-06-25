class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        count = 0
        while l < r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
            elif people[r] <= limit:
                r -= 1
            else:
                l += 1

            count += 1

        return 1 + count if l == r else count