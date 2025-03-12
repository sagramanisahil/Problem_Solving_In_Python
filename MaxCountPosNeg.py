class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        MaxPos = 0
        MaxNeg = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                MaxPos += 1
            elif nums[i] < 0:
                MaxNeg += 1
        if MaxPos > MaxNeg:
            return MaxPos
        else:
            return MaxNeg