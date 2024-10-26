class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        x, y = 0,0
        words = []

        word = 1
        while x < A and y < B:
            if word == 1:
                words.append(word1[x])
                x += 1
                word = 2
            else:
                words.append(word2[y])
                y += 1
                word = 1
        
        while x < A:
            words.append(word1[x])
            x += 1
        
        while y < B:
            words.append(word2[y])
            y += 1

        return ''.join(words)
        