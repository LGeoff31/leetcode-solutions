class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        2: 000010
        3: 000011
        5: 000101
        7: 000111

        11: 1011
        13: 1101
        15: 1111

        31: 11111
        """
        res = []
        for n in nums:
            if n % 2 == 0:
                res.append(-1)
                continue
            bin_rep = ["0"] * (32 - len(bin(n)[2:])) + list(bin(n)[2:])
            number_ones = 0
            for i in range(len(bin_rep) - 1, -1, -1):
                if bin_rep[i] == "1":
                    number_ones += 1
                else:
                    bin_rep[i+1] = "0"
                    break   
            res.append(int("".join(bin_rep), 2))
        return res