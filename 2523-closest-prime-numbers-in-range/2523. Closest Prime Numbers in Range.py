class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right + 1)]
        prime[0], prime[1] = False, False
        p = 2
        while p * p <= right + 1:
            if prime[p] == True:
                for i in range(p*p, right + 1, p):
                    prime[i] = False
            p += 1

        first, second = None, None
        res = [-1, -1]
        for i in range(left, right + 1):
            if prime[i]:
                if not first:
                    first = i
                elif not second:
                    second = i
                    res = [first, second]
                    print(res)
                else:
                    if i - second < res[-1] - res[0]:
                        res = [second, i]
                    first = second
                    second = i
        return res
                
                



