class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prf = strs[0]
        prf_len = len(strs)
        for i in strs[1:]:
            while prf != i[0:prf_len]:
                prf_len -= 1
                if prf_len == 0:
                    return ""
                prf = prf[0:prf_len]
        return prf