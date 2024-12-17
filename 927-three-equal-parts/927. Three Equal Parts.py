class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = arr.count(1)
        if ones % 3 != 0: return [-1, -1]
        if ones == 0: return [0, len(arr) - 1]

        ones_per_part = ones // 3

        first = second = third = -1
        count = 0
        
        for i, bit in enumerate(arr):
            if bit == 1:
                count += 1
                if count == 1: 
                    first = i
                elif count == ones_per_part + 1:
                    second = i
                elif count == 2*ones_per_part+1:
                    third = i
        while third < len(arr) and arr[first] == arr[second] == arr[third]:
            first += 1
            second += 1
            third += 1
        print(first, second, third)
        if third == len(arr):
            return [first - 1, second]
        return [-1, -1]
            