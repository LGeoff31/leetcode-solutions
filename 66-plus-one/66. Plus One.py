class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = "".join(list(str(d) for d in digits))
        b = str(int(a) + 1)
        return list(int(z) for z in b)