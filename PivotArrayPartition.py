class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        for i in range(n):
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1
        mid = left

        for i in range(n):
            if nums[i] == pivot:
                result[left] = pivot
                left += 1
            
        for i in range(n):
            if nums[i] > pivot:
                result[left] = nums[i]
                left += 1
        return result