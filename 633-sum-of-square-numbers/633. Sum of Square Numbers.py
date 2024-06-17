class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #We know the highest one of hte numbers can do is math.ceil(math.sqrt(c))
        if c==0: return True
        def check_perfect_square(n): #O(sqrt(n))
            for i in range(1 + math.floor(math.sqrt(n))):
                if i**2 == n:
                    return True
            return False
        highest_num = math.ceil(math.sqrt(c))
        perfect_squares = set()
        for i in range(math.ceil(math.sqrt(2**31))):
            perfect_squares.add(i**2)
        for i in range(highest_num): #O(sqrt(c))
            if c - i**2 in perfect_squares: #O(sqrt(c))
                return True
        #O(C)
        return False
        