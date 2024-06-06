class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        #basically same a binary but all the even indicies are negative
        lst = []

        while n != 0:
            rem = n % 2
            lst.append(str(rem))
            n =- (n // 2)
            print(n)
        return "".join(lst[::-1])

        