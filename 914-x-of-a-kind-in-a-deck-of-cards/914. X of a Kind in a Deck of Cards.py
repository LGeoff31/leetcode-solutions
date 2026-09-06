class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)
        x = min(freq.values()) # find the smallest factor > 1
        possible_x = [x]
        print(freq)
        if x <= 1: possible_x.pop()
        for i in range(2, x):
            if x % i == 0:
                possible_x.append(i)
        if not possible_x: return False
        for x in possible_x:
            if all(freq[key] % x == 0 for key in freq):
                return True 
        return False