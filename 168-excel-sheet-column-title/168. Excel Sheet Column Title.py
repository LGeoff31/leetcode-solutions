class Solution:
    def convertToTitle(self, a: int) -> str:
        res = ""
        while a:
            a -= 1  # Decrement to adjust for 1-based index (Excel column naming)
            res += chr(a % 26 + ord('A'))  # Map remainder to corresponding letter
            a //= 26  # Move to the next place value

        return res[::-1]  # Reverse the result to get the correct column name
