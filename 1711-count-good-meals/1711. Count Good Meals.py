class Solution:
    def countPairs(self, lst: List[int]) -> int:
        MOD = 10 ** 9 + 7
        print(len(lst))
        # Max value is 2^20, theres around log(2^20) options for the complement (1048576)
        a = set(lst)
        powers_two = [2**i for i in range(23)]
        print(powers_two)
        def power_two(num): #O(logm)
            while num != 1:
                if num%2 != 0:
                    return False 
                num //= 2
            return True
        b = Counter(lst)
        res = 0
        lst = list(set(lst))
        for i in range(len(lst)): #O(n)
            for num in powers_two:
                if num > lst[i] and (num - lst[i]) in a and (num - lst[i]) > lst[i]:
                    res += b[lst[i]] * b[num - lst[i]]
                    print(lst[i], num-lst[i])
            print(res)
        for key in b:
            if key+key in powers_two:
                res += (b[key] * (b[key] - 1)) // 2

        return res % MOD
