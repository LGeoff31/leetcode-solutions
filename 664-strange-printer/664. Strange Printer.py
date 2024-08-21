class Solution:
    def strangePrinter(self, s: str) -> int:
        # Preprocess the string to remove consecutive duplicate characters
        s = "".join(char for char, _ in itertools.groupby(s))

        memo = {}

        def _minimum_turns(start, end) -> int:
            # Base case: empty string requires 0 turns
            if start > end:
                return 0

            # If result is memoized, return it
            if (start, end) in memo:
                return memo[(start, end)]

            # Initialize with worst case: print each character separately
            min_turns = 1 + _minimum_turns(start + 1, end)

            # Try to optimize by finding matching characters
            for k in range(start + 1, end + 1):
                if s[k] == s[start]:
                    # If match found, try splitting the problem
                    turns_with_match = _minimum_turns(
                        start, k - 1
                    ) + _minimum_turns(k + 1, end)
                    min_turns = min(min_turns, turns_with_match)

            # Memoize and return the result
            memo[(start, end)] = min_turns
            return min_turns

        # Start the recursive process
        return _minimum_turns(0, len(s) - 1)
