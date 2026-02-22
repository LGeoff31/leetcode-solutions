class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        """
        can have up to 9 digits, 9! permutations of n, 362,880
        """

        def generate_permutations(n):
            n_str = str(n)
            return ["".join(p) for p in permutations(n_str)]

        lst = generate_permutations(n)
        res = 0
        for c in str(n):
            res += factorial(int(c))
        return str(res) in lst
            