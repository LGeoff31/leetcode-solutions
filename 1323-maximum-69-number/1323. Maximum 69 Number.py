class Solution:
    def maximum69Number (self, num: int) -> int:
        if str(num).count("6") == 0: return num
        a = [c for c in str(num)]
        for i in range(len(a)):
            if a[i] == "6":
                a[i] = "9"
                break
        
        return int("".join(a))