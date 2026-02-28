class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary_str = ""
        MOD = 10 ** 9 + 7
        for i in range(1, n+1):
            binary_str += bin(i)[2:]

        return int(binary_str, 2) % MOD 