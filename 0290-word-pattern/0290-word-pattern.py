class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for char,word in zip(pattern,words):
            if char not in charToWord:
                charToWord[char] = word
            elif charToWord[char] != word:
                return False
            
            if word not in wordToChar:
                wordToChar[word] = char
            elif wordToChar[word] != char:
                return False
        
        return True