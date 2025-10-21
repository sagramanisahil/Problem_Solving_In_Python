class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        values = []
        
        def backtrack(start):
            if len(values) == k:
                result.append(values[:])
                return
            for num in range(start, n+1):
                values.append(num)
                backtrack(num+1)
                values.pop()
        backtrack(1)
        return result