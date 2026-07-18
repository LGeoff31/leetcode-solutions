class Solution:
    def sum(self, num1: int, num2: int) -> int:
        """
        num1 -> 23
        num2 -> 35

        23: 00010111
        35: 00100011
        58: 00111010 -> 32+16+8+2 = 58

        """
        if num1 < 0 or num2 < 0:
            print('cheated')
            return num1 + num2

        def convert_to_padded_binary_string(num):
            bin_string = bin(num)[2:]
            length = len(bin_string)
            return (32 - length) * "0" + bin_string 
        res = 0 
        b1, b2 = convert_to_padded_binary_string(num1), convert_to_padded_binary_string(num2)
        carry = 0
        for i in range(len(b1) -1, -1, -1):
            column_sum = int(b1[i]) + int(b2[i]) + carry
            if column_sum == 1 or column_sum == 3:
                res |= (1 << (31-i))
            carry = 1 if column_sum >= 2 else 0
        return res