class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverseInt = 0
        copy = x

        while x > 0:
            reverseInt = (reverseInt * 10) + (x % 10)
            x //= 10
        return reverseInt == copy