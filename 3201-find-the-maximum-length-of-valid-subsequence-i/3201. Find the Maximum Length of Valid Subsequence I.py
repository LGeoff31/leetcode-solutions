class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        a,b,c,d = 0, 0, 0, 0
        # 1: all even
        for n in nums:
            if n % 2 == 0:
                a += 1
        # 2: all odd
        for n in nums:
            if n % 2 == 1:
                b += 1
        # 3: even odd even odd
        even = True
        for n in nums:
            if even:
                if n%2 == 0:
                    c += 1
                    even = not even
            else:
                if n%2 == 1:
                    c += 1
                    even = not even
        # 4: odd even
        even = False
        for n in nums:
            if even:
                if n%2 == 0:
                    d += 1
                    even = not even
            else:
                if n%2 == 1:
                    d += 1
                    even = not even
        return max(a,b,c,d)