class Solution:
    def fib(self, n: int) -> int:
        """
        fib(n) = golden_ratio^n - complement_golden_ratio^n
        """
        golden_ratio = (1 + sqrt(5)) / 2

        return round((golden_ratio ** n - ((1-sqrt(5)) / 2) ** n) / sqrt(5))