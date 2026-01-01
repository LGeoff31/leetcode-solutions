class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(int(z) for z in str(int("".join(list(str(d) for d in digits))) + 1))