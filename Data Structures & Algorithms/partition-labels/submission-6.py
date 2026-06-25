class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}

        for i, v in enumerate(s):
            hash_map[v] = i
        size = 0
        end = 0
        output = []
        for i in range(len(s)):
            size += 1
            last_index = hash_map[s[i]]
            if last_index > end:
                end = last_index

            if i == end:
                output.append(size)
                size = 0
        
        return output