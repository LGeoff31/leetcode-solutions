class Solution:
    def smallestPalindrome(self, s: str) -> str:
        dic = Counter(s)
        lst = sorted([(key, dic[key]) for key in dic])
        res = ""
        if len(s) == 1: return s
        odd_letter = ""

        for letter, freq in lst:
            if freq % 2 == 1:
                odd_letter = letter
            res += letter * (freq // 2)
        if odd_letter: 
            temp_res = res
            res += odd_letter
            res += temp_res[::-1]
        else:
            res += res[::-1]
            

        return res