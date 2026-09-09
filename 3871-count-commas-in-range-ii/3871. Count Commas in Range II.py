class Solution:
    def countCommas(self, n: int) -> int:
        """
        1,000 - 999,999: 1 comma
        1,000,000 - 999,999,999 - 2 commas
        1,000,000,000 - 999,999,999,999 - 3 commas

        999,999 -> 999,000

         v -> 999,002

        """
        if n < 1000:
            return 0

        res = 0
        cnt = 1

        lower_bound = 1_000
        upper_bound = 999_999

        while True:
            # Inside the intervals
            if lower_bound <= n <= upper_bound: 
                res += (n - lower_bound + 1) * cnt
                break
            else: # Covers the whole interval, go next intervals
                res += (upper_bound - lower_bound + 1) * cnt 
                upper_bound = upper_bound * 1000 + 999
                lower_bound *= 1000
                cnt += 1

        return res