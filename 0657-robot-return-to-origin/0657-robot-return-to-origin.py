class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = list(moves)

        countU = moves.count('U')
        countD = moves.count('D')
        countL = moves.count('L')
        countR = moves.count('R')

        if countU == countD and countL == countR:
            return True
        else:
            return False