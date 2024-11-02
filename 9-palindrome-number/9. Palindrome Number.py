class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        lst = []
        while x != 0:
            lst.append(x%10)
            x//=10
            print(x)
        print(lst)
        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True