class Solution:
    def fractionAddition(self, expression: str) -> str:
        lst = re.split("[+-]", expression)
        def gcd(a,b): 
            if b == 0:
                return a
            return gcd(b, a % b)
        def lcm(a,b):
            return a*b//gcd(a,b)
        def get_num_den(expr):
            num, den = expr.split("/")
            return int(num), int(den)
        operations = []
        for i, c in enumerate(expression):
            if c in "-+" and i != 0: operations.append(c)
        num, den = get_num_den("-" + lst[1] if not lst[0] else lst[0])
        idx = 0
        if not lst[0]: lst = lst[1:]
        for i in range(1, len(lst)):
            n, d = get_num_den(lst[i])
            if operations[idx] == '-':
                n *= -1
            common_divisor = lcm(den, int(d))
            num = num * (common_divisor // den) + n * (common_divisor // d)
            den = common_divisor
            idx += 1
        z = gcd(num, den)
        num //= z
        den //= z
        # if num == 0: return 0
        return f"{num}/{den}"