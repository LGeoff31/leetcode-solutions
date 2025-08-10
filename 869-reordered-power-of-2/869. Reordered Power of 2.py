class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        dic = set()
        for i in range(100):
            dic.add(str(2**i))
        def match(a,b):
            if Counter(a) == Counter(str(b)):
                return True
            return False
        for key in dic:
            if match(key, n):
                return True
        return False