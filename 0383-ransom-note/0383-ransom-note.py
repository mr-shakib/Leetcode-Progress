from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cRansomNote = Counter(ransomNote)
        cMagazine = Counter(magazine)
        for char, count in cRansomNote.items():
            if cMagazine[char] < count:
                return False
        return True