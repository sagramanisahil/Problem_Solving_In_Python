class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        count = 0

        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    baskets[j] = -1
                    count += 1
                    break
        return n - count