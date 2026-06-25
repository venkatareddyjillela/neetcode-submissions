class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort (swap adjacent elements if it is in wrong order)
        # return self.bubble_sort(nums)
        # selection sort (select smallest or largest number and place it in correct place)
        # return self.selection_sort(nums)
        # insertion sort 
            # (select element starting from second place and compare it with previous elements and 
            # insert at correct place on ascending order right side)
        # return self.insertion_sort(nums)
        # Quick sort 
            # Chose pivot(first, last or random index)
            # compare pivot with all elements and place smaller than pivot on left side and larger on right side
            # repeat same step on left and right side untill single or no elments are available
        # self.quick_sort(nums, 0, len(nums)-1)
        # return nums
        # merge sort
            # divide and conquer
            # divide: divide array untill it can't be split
            # conquer: merge each element in sorted order
        
        self.merge_sort(nums, 0, len(nums)-1)
        return nums

    def merge(self, nums, l, m, r):
        left, right = nums[l:m+1], nums[m+1:r+1]
        i, j, k = 0, 0, l
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1
        
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid+1, right)
        self.merge(nums, left, mid, right)
    
    def quick_sort(self, nums, low, high):
        if low < high:
            partition_index = self.partition(nums, low, high)
            self.quick_sort(nums, low, partition_index-1)
            self.quick_sort(nums, partition_index+1, high)

    def partition(self, nums, l, r):
        pivot = l
        i, j = l, r
        while i < j:
            while nums[i] <= nums[pivot] and i < r:
                i += 1

            while nums[j] > nums[pivot] and j > l:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            
        nums[pivot], nums[j] = nums[j], nums[pivot]
        return j
        

        

    def insertion_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            l = i
            while l > 0 and nums[l] < nums[l-1]:
                nums[l], nums[l-1]= nums[l-1], nums[l]
                l -= 1
        return nums


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