class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        rev = list(reversed(st))
        res = ' '.join(rev)
        return res