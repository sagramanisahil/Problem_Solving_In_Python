class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float(inf)

        for i in range(len(nums)-2):
            left, right = i + 1, len(nums)-1
            
            while left < right:
                ans = nums[i] + nums[left] + nums[right]

                if ans == target:
                    return ans
                elif ans < target:
                    left += 1
                else:
                    right -= 1
                if abs(ans - target) < abs(result - target):
                    result = ans
        return result