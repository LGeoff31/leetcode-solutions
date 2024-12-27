class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9: return n
        # 1-9 -> ones
        # 10-99 -> 90 twos
        # 100 -> 999 -> 900 threes
        lst = [9, 180, 2_700, 36_000, 450_000, 5_400_000, 63_000_000, 720_000_000, 8_100_000_000]
        prefix = list(accumulate(lst))
        digit = bisect_left(prefix, n) + 1
        n -= prefix[digit - 2]
        string = ""
        val = n // digit
        rem = n % digit
        print(val, rem, n, digit)
        if rem > 0:
            return int(str((10 ** (digit - 1) + val - 1) + 1)[rem-1])
        else:
            return int(str(10 ** (digit - 1) + val - 1)[-1])
        # for i in range(10 ** (digit-1), 10 ** (digit)):
        #     string += str(i)
        #     if len(string) >= n: break

        # print(digit, n)
        # print(string)
        # return int(string[n-1])
