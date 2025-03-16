class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = Counter(s)
        odd = 0
        for key in dic:
            odd += dic[key] % 2
        return odd <= 1