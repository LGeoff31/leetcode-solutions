class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = 1 + candies[i]
        
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = 1 + candies[i]
        return sum(candies)
        