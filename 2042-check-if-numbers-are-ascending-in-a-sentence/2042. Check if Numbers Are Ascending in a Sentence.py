class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a = s.split()
        lst = []
        for b in a:
            if b.isdigit():
                lst.append(b)
        valid = True
        print(lst)
        for i in range(1, len(lst)):
            if int(lst[i]) <= int(lst[i-1]):
                valid = False
        return valid
        