class Solution:
    def reformat(self, s: str) -> str:
        letters, numbers = list(c for c in s if c.isalpha()), list(c for c in s if c.isnumeric())
        if abs(len(letters) - len(numbers)) > 1:
            return ""
        
        if len(letters) > len(numbers):
            res = letters[0]
            for i in range(len(numbers)):
                res += numbers[i] + letters[i+1]
        
        elif len(letters) < len(numbers):
            res = numbers[0]
            for i in range(len(letters)):
                res += letters[i] + numbers[i+1]
        else:
            res = ""
            for i in range(len(letters)):
                res += letters[i] + numbers[i]
        return res