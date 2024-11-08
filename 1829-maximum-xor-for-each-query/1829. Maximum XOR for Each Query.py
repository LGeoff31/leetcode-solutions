class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix = []
        a = 0
        for num in nums:
            a ^= num
            prefix.append(a)
        res = []
        for i in range(len(prefix) -1, -1, -1):
            currXOR = prefix[i]
            string = "0" * (32 - len(bin(currXOR)[2:])) + bin(currXOR)[2:]
            # print(string)
            num = 0
            for i in range(len(string) -1, -1, -1):
                if string[i] == "0":
                    if num + (1 << (32-i-1)) < 2**maximumBit:
                        num += 1 << (32-i-1)
                    else:
                        break
                    # print(num)

            res.append(num)
        return res