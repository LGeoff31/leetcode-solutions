class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Food: (rating, cuisine)
        # Cuisine: (rating, food)
        n = len(foods)
        self.f = {}
        self.c = defaultdict(SortedList)
        for i in range(n):
            self.f[foods[i]] = [ratings[i], cuisines[i]]
            self.c[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating, cuisine = self.f[food]
        self.c[cuisine].remove((-oldRating, food))
        self.f[food] = (newRating, cuisine)
        self.c[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.c[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)