class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = [0] * (n+1)
        print(lst)
        for i in range(n+1):
            number_1 = 0
            mask = 1
            for j in range(32):
                if i & mask:
                    number_1 += 1
                mask <<= 1
            lst[i] = number_1
        return lst

            
        