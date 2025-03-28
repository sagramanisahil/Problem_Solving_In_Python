class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxDifference = 0

        for i in range (1, len(nums)):
            maxDifference = max(maxDifference, nums[i] - nums[i-1])
        return maxDifference
        