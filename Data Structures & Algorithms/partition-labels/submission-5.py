class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = defaultdict(list)

        for i, v in enumerate(s):
            if len(hash_map[v]) > 1:
                hash_map[v][-1] = i
            else:
                hash_map[v].append(i)
        min_heap = list(hash_map.values())
        heapq.heapify(min_heap)

        output = []
        while min_heap:
            curr_range = heapq.heappop(min_heap)
            if min_heap and len(curr_range) > 1 and curr_range[1] > min_heap[0][0]:
                next_range = heapq.heappop(min_heap)
                heapq.heappush(min_heap, [curr_range[0], max(curr_range[1], next_range[-1])])
            else:
                if len(curr_range) > 1:
                    output.append(curr_range[1] - curr_range[0] + 1)
                else:
                    output.append(1)
        
        return output