class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            num = nums[i]
            if num in result:
                continue
            count = 0
            for j in range(len(nums)):
                if nums[j] == num:
                    count += 1
            if count > len(nums) // 3:
                result.append(num)
        return result