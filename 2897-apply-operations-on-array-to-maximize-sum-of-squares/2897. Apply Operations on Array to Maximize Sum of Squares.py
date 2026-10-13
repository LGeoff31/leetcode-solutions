from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        """
        [2,6,5,8]

        2: 0010
        6: 0110
        5: 0101
        8: 1000

        the number of bits in each 'col' doesn't change
        just need to redistribute

        greedy: want to first build biggest number possible with the bits, because it's a sum of squares

        {0: 1, 1: 2, 2: 2, 3:1}
        can build first biggest: 1+2+4+8=15
        {0: 0, 1: 1, 2: 1, 3:0}
        can build second: 2+4=6
        
        """

        # make the hashmap
        bits = defaultdict(int)

        for n in nums:
            bin_ver = bin(n)[2:]
            length = len(bin_ver)
            for i in range(length):
                if bin_ver[i] == "1":
                    bits[length - i - 1] += 1
            
        # print(bits)

        res = 0
        for _ in range(k):
            biggest = 0
            for key in bits.keys():
                if bits[key] >= 1:
                    biggest += 2**key
                    bits[key] -= 1

            res += biggest ** 2

        return res % (10**9 + 7)