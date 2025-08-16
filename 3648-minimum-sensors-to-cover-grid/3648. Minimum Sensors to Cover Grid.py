class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        """
        0000000000
        0000000000
        0000000000
        0000000000
        0000000000
        """
        w, h = ceil(n/(1+2*k)), ceil(m/(1+2*k))
        return w*h