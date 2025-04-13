class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulus = 10**9 + 7
        Even = (n + 1) // 2
        Odd = n // 2
        return (pow(5, Even, modulus) * pow(4, Odd, modulus)) % modulus