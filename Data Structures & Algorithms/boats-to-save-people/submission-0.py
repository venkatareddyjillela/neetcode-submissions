class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l, r = 0, len(people)-1

        while l<r:
            if people[r] == limit:
                boats += 1
                r -= 1

            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            # elif people[l] + people[r] > limit:
            else:
                boats += 1
                r -= 1
        
        if l == r:
            boats += 1

        return boats

