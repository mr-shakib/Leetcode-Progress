class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = 1
        n = len(ratings)
        ratings.sort()
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                candy += 2
            else:
                candy += 1
        return candy