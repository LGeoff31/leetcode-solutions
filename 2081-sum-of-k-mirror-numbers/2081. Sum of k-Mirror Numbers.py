class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """
        How to generate list of palindromes in increasing order
        """
        def to_base_k(num: int, k: int) -> str:
            res = []
            while num > 0:
                res.append(str(num % k))
                num //= k
            return ''.join(res[::-1])

        def generate_palindromes():
            length = 1
            while True:
                # Odd-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])
                # Even-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])
                length += 1
        res = 0
        count = 0
        for num in generate_palindromes():
            a = to_base_k(num, k)
            if str(a) == str(a)[::-1]:
                res += num
                count += 1
                if count == n:
                    break
        return res