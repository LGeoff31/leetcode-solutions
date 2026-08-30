class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        def decode_value(num):
            width = num % 10
            d = num // 10

            x,y = int(str(d)[:width]), int(str(d)[width : ])
            return pow(x, y, 10 ** 9 + 7)
            
        MOD = 10 ** 9 + 7

        res = 0
        for num in nums:
            res += decode_value(num)

        return res % MOD