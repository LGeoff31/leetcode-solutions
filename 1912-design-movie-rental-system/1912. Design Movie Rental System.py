class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedList) # (price, shop, movie)
        self.rented_movies = defaultdict(SortedList) #(price, shop, movie)
        self.rented_movies_org = SortedList()
        self.find_price = {}
        for a,b,c in entries:
            self.movies[b].add((c,a,b))
            self.find_price[(a,b)] = c

    def search(self, movie: int) -> List[int]:
        return [b for _,b,_ in self.movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.find_price[(shop, movie)]
        self.movies[movie].remove((p, shop, movie))
        self.rented_movies[movie].add((p, shop, movie))
        self.rented_movies_org.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.find_price[(shop, movie)]
        self.rented_movies[movie].remove((p, shop, movie))
        self.rented_movies_org.remove((p, shop, movie))
        self.movies[movie].add((p, shop, movie))

    def report(self) -> List[List[int]]:
        return [(b,c) for _,b,c in self.rented_movies_org[:5]]
        # return [[b,c] for _,b,c in self.rented_movies_org[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()