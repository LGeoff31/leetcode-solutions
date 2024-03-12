class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            result += dic[s[i]]
            if i > 0:
                if (s[i] == "V" or s[i] == "X") and s[i-1] == "I":
                    result -= 2
                if (s[i] == "L" or s[i] == "C") and s[i-1] == "X":
                    result -= 20
                if (s[i] == "D" or s[i] == "M") and s[i-1] == "C":
                    result -= 200
        return result
            
            










        # value = 0
        # dic = {'I': 1, "V": 5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        # i = 0
        # while i <= len(s) - 2:
        #     value += dic[s[i]]
        #     if (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C") or (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"))):
        #         value += dic[s[i+1]]
        #         value -= 2 * dic[s[i]]
        #         i += 1
        #     i += 1
        
        # if i < len(s):
        #     value += dic[s[i]]
        # return value

        
            
            
            
                    
        
        


