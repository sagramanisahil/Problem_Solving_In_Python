class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        even_count = 1
        odd_count = 0
        parity = 0

        for v in s:
            if v in vowels:
                parity ^= 1
            if parity == 0:
                even_count += 1
            else:
                odd_count += 1

        return even_count * odd_count > 0