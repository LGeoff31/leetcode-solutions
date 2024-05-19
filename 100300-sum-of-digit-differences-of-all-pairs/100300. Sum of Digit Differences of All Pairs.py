class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        digits = []

        n = len(str(nums[0]))

        for i in range(n):
            arr = []
            for n in nums:
                arr.append(int(str(n)[i]))
            arr.sort()
            digits.append(arr)


        res = 0

        print("digits", digits)
        for arr in digits:
            freq = Counter(arr)
            z = len(arr)
            print(freq)
            for key in freq:
                # print("bisect_right", bisect.bisect_right(arr, key))
                res += freq[key] * (z - (bisect.bisect_right(arr, key)))

        return res

        