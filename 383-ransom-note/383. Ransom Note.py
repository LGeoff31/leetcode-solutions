class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}
        b = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in a:
                a[ransomNote[i]] = 1
            else:
                a[ransomNote[i]] += 1
        for i in range(len(magazine)):
            if magazine[i] not in b:
                b[magazine[i]] = 1
            else:
                b[magazine[i]] += 1
        for key in a:
            if key not in b:
                return False
            if a[key] > b[key]:
                return False
        return True
