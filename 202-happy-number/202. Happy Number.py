class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visited = set()
        
        while True:
            if n in visited:
                return False
            visited.add(n)
            a = list(str(n))
            total = 0
            for char in a:
                total += int(char) * int(char)
            n = total
            if n == 1:
                return True

        