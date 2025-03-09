class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        low = 0

        for high in range (n + k - 1):
            if high > 0 and colors[high % n] == colors[(high-1) % n]:
                low = high
        
            if(high - low + 1) >= k:
                count += 1
        return count
