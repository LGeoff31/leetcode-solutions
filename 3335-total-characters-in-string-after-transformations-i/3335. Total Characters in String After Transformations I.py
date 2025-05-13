class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1

        for i in range(t):
            new_count = [0] * 26
            for i in range(len(count)):
                if count[i] > 0:
                    letter = chr(i + 97)
                    if letter == "z":
                        new_count[0] = (new_count[0] + count[25]) % MOD
                        new_count[1] = (new_count[1] + count[25]) % MOD
                    else:
                        new_count[i+1] = (new_count[i+1] + count[i]) % MOD
            count = new_count.copy()

        return sum(count) % MOD