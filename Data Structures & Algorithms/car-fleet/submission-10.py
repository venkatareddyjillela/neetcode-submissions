class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        for i in range(len(position)):
            fleet.append((position[i], speed[i]))
        
        fleet.sort()

        count = 0
        print(fleet)
        while fleet:
            if len(fleet) < 2:
                count += 1
                break
            first, second = fleet.pop(), fleet.pop()
            t1 = (target - first[0])/first[1]
            t2 = (target - second[0])/second[1]
            if t2 > t1:
                count += 1
                fleet.append(second)
            else:
                fleet.append(first)
    
        return count
