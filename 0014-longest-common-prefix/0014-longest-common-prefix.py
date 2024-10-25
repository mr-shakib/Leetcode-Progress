class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(len(s) for s in strs)
        for i in range (shortest):
            if not all(s[i] ==strs[0][i] for s in strs):
                return strs[0][:i]
        return strs[0][:shortest]