class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_maximum_amount(nums):
            nocount = count = 0
            for i in nums:
                temp = max(count, nocount + i)
                nocount = count
                count = temp
            return count

        if len(nums) == 1:
            return nums[0]

        return max(get_maximum_amount(nums[:-1]), get_maximum_amount(nums[1:]))
