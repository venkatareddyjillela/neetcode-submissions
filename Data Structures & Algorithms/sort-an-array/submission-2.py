import random
class Solution:
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     low, high = 0, len(nums)-1
    #     self.quick_sort(nums, low, high)
    #     return nums

    # def quick_sort(self, nums, low, high):
    #     if low < high:
    #         partition_index = self.partition(nums, low, high)
    #         self.quick_sort(nums, low, partition_index-1)
    #         self.quick_sort(nums, partition_index+1, high)

    # def partition(self, nums, low, high):
    #     i, j = low, high
    #     pivot_index = random.randint(low, high)
    #     pivot = nums[pivot_index]

    #     while i < j:
    #         while nums[i] <= pivot and i < high:
    #             i += 1
            
    #         while nums[j] > pivot and j > low:
    #             j -= 1
            
    #         if i < j:
    #             self.swap(nums, i, j)
        
    #     self.swap(nums, pivot_index, j)
    #     return j
        
    # def swap(self, nums, low, high):
    #     nums[low], nums[high] = nums[high], nums[low]

    # selection sort
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums)):
    #         mini = i
    #         for j in range(i+1, len(nums)):
    #             if nums[j] < nums[mini]:
    #                 mini = j
    #         nums[i], nums[mini] = nums[mini], nums[i]
    #     return nums

    # Bubble sort
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
