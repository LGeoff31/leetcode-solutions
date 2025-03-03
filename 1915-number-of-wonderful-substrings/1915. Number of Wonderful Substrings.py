class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefix_map = defaultdict(int) # maps binary string to a frequency
        prefix_map[0] = 1
        binary = [0] * 10
        mask = 0
        res = 0

        # aabb

        for char in word:
            mask ^= (1 << ord(char) - ord("a"))
            # binary[ord(char) - ord('a')] ^= 1
            # bin_str = "".join(list(str(num) for num in binary))
            cnt = prefix_map[mask]
            # check wonderful substrings
            # print("FOR X")
            prefix_map[mask] += 1

            for i in range(10):
                mask ^= 1 << i
                # binary[i] ^= 1
                cnt += prefix_map[mask]
                # print("".join(list(str(num) for num in binary)), bin_str, prefix_map["".join(list(str(num) for num in binary))])
                mask ^= 1 << i

                # binary[i] ^= 1
            print(cnt)
            res += 1 if cnt == 0 else cnt
        return res