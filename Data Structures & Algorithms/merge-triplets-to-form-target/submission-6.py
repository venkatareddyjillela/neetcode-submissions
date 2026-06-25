class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        for triplet in triplets:
            valid_triplet = True
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    valid_triplet = False
                    break
            if valid_triplet:
                valid.append(triplet)
        
        max_array = [-float('inf')] * len(target)
        for triplet in valid:
            for i in range(len(triplet)):
                max_array[i] = max(max_array[i], triplet[i])

        for i in range(len(target)):
            if max_array[i] != target[i]:
                return False
        
        return True
        