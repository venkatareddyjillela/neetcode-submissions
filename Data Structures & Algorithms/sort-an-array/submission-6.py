class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort (swap adjacent elements if it is in wrong order)
        # return self.bubble_sort(nums)
        # selection sort (select smallest or largest number and place it in correct place)
        return self.selection_sort(nums)
        # insertion sort 
            # (select element starting from second place and compare it with previous elements and 
            # insert at correct place on ascending order right side)
        # Quick sort 
            # Chose pivot(first, last or random index)
            # compare pivot with all elements and place smaller than pivot on left side and larger on right side
            # repeat same step on left and right side untill single or no elments are available
        # merge sort
            # divide and conquer
            # divide: divide array untill it can't be split
            # conquer: merge each element in sorted order

    def selection_sort(self, nums):
        def get_min_index(l):
            curr = nums[l]
            ind = l
            for i in range(l, n):
                if curr > nums[i]:
                    curr = nums[i]
                    ind = i
            return ind

        l = 0
        n = len(nums)
        while l < n:
            ind = get_min_index(l)
            nums[l], nums[ind] = nums[ind], nums[l]
            l += 1
        return nums

    def bubble_sort(self, nums):
        n = len(nums)
        for last in range(n-1, 0, -1):
            swapped = False
            i = 0
            while i < last:
                if nums[i] > nums[i+1]:
                    nums[l], nums[r] = nums[r], nums[l]
                    swapped = True
                i += 1
            
            if not swapped:
                return nums
        return nums