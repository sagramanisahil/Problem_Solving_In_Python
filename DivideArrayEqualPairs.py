class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] == nums[i+1]:
                count += 1
        return count == len(nums) // 2