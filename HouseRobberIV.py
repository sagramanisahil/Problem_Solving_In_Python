class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_steal_money(steal_capability):
            c = 0
            i = 0
            while i < len(nums):
                if nums[i] <= steal_capability:
                    c += 1
                    i += 2
                else:
                    i += 1
            return c >= k
        l, r = min(nums), max(nums)
        while l < r:
            mid = (l + r) // 2
            if can_steal_money(mid):
                r = mid
            else:
                l = mid + 1
        return l