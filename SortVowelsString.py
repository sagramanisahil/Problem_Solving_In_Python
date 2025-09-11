class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch in "AEIOUaeiou"]
        vowels.sort()
        index = 0
        result = list(s)
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                result[i] = vowels[index]
                index += 1
        return "".join(result)
