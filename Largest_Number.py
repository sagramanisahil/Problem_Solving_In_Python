class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_list = []
        for num in nums:
            string_list.append(str(num))
        n = len(string_list)
        for i in range(n):
            for j in range(i+1, n):
                if string_list[i] + string_list[j] < string_list[j] + string_list[i]:
                    string_list[i], string_list[j] = string_list[j], string_list[i]
        result = ''.join(string_list)
        if result[0] == '0':
            return '0'
        return result