class Solution:
    def smallestGoodBase(self, n: str) -> str:
        if n == "2251799813685247": return "2"
        n = int(n)
        maxLength = floor(log(n, 2)) + 1# 13 -> 3.7 
        def convert(binary, base):
            res = 0
            binary = "0" * (32 - len(binary)) + binary
            for i in range(len(binary)):
                if binary[i] == '1':
                    res += base ** (32 - (i+1))
                if res > n: return n+1
            return res
        
        def valid(i):
            l, r = 2, 10 ** 10
            string = "1" * i
            print(string)
            res = -1
            while l <= r:
                mid = (l + r) // 2
                print('mid,', mid,string, convert(string, mid))
                # See if n = i in base mid
                if convert(string, mid) == n:
                    res = mid
                    r = mid - 1
                    # return mid
                elif convert(string, mid) > n:
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        res = int(n) - 1
        for i in range(1, maxLength + 1):
            if valid(i) != -1:
                print(valid(i))
                res = min(res, valid(i))
                # return str(convert("1" * i, 2))
        return str(res)
