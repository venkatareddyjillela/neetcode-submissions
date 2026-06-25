class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i, v in enumerate(target):
                if v == triplet[i]:
                    valid.add(i)
        
        return len(valid) == 3