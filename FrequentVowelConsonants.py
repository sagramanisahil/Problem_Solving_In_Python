class Solution:
    def maxFreqSum(self, s: str) -> int:
        consonants = 0
        vowels = 0

        string_set = set(s)
        for i in string_set:
            if i in "aeiou":
                vowels = max(vowels, s.count(i))
            else:
                consonants = max(consonants, s.count(i))
        return vowels + consonants