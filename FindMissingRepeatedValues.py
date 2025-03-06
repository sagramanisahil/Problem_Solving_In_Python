class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # result []
        n: int = len(grid)
        size: int = n * n
        frequent: List[int] = [0] * (size+1)
        r: int = -1
        m: int = -1
        for row in grid:
            for num in row:
                frequent[num] += 1
        for num in range(1, size+1):
            if frequent[num] == 2:
                r = num
            if frequent[num] == 0:
                m = num
        return [r, m]