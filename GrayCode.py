class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray = [i ^ (i//2) for i in range(pow(2,n))]
        return gray