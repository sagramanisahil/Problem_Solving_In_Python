class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = {}
        result = 0

        for answer in answers:
            if answer == 0:
                result += 1
            elif answer in counter and counter[answer] > 0:
                counter[answer] -= 1
            else:
                result += answer + 1
                counter[answer] = answer
        return result