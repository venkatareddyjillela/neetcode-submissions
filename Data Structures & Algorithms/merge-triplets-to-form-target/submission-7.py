class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        max_array = [-float('inf')] * 3
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            max_array[0] = max(max_array[0], triplet[0])
            max_array[1] = max(max_array[1], triplet[1])
            max_array[2] = max(max_array[2], triplet[2])

        for i in range(len(target)):
            if max_array[i] != target[i]:
                return False
        
        return True