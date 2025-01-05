class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def valid_word(word):
            # Cannot contain leading zeros
            if word[0] == "0" and len(word) > 1: return False
            # Must be all digits
            allDigits = sum([num.isdigit() for num in word]) == len(word)
            if not allDigits: return False
            # Must strictly be numbers from 0 <= x <= 255
            return 0 <= int(word) <= 255

        def IPv4(string):
            x_lst = string.split(".")
            if len(x_lst) != 4: return False
            for num in x_lst:
                if len(num) == 0: return False
            print(x_lst)
            return valid_word(x_lst[0]) and valid_word(x_lst[1]) and valid_word(x_lst[2]) and valid_word(x_lst[3])
        def validWord(word):
            if not(1 <= len(word) <= 4): return False
            # Has obsecure character
            for c in word:
                if not(c.isdigit() or c in "abcdefABCDEF"): return False
            return True
        def IPv6(string):
            x_lst = string.split(":")
            if len(x_lst) != 8: return False
            for num in x_lst:
                if len(num) == 0: return False
            valid = True
            for word in x_lst:
                valid = valid and validWord(word)
            return valid


        return "IPv4" if IPv4(queryIP) else "IPv6" if IPv6(queryIP) else "Neither"