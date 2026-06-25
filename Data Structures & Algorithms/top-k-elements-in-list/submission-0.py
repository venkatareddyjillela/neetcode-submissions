class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            arr[freq].append(num)
        print("arr:", arr)
        res = []
        for i in range(len(arr)-1, -1, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res