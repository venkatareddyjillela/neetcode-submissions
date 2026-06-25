class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hash_map = defaultdict(int)
        hash_map = {}
        n = len(hand)
        if n % groupSize:
            return False
        for i in hand:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        total_groups = n // groupSize
        start = min(hash_map.keys())
        while total_groups:
            new_start = None
            if start is None:
                start = min(hash_map.keys())
            for i in range(start, start+groupSize):
                # if hash_map[i] == 0:
                #     return False
                if i not in hash_map:
                    return False
                if new_start is None and hash_map[i] > 1:
                    new_start = i
                if hash_map[i] > 1:
                    hash_map[i] -= 1
                else:
                    hash_map.pop(i)
            start = new_start
            total_groups -= 1
        return True