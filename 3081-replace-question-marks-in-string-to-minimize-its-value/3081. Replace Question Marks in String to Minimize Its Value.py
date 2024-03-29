class Solution:
    def minimizeStringValue(self, s: str) -> str:
        lst = [0] * 26
        for letter in s:
            if letter != '?':
                lst[ord(letter) - ord("a")] += 1
        res = ""
        number_to_letter = {i: chr(97 + i) for i in range(26)}
        a = []
        for letter in s:
            if letter != "?":
                # res+=letter
                # a.append(letter)
                continue
            else:
                num = lst.index(min(lst))
                # print(num, lst)
                a.append(number_to_letter[num])
                # res+=number_to_letter[num]
                lst[num]+=1

        # print(a)
        a.sort()
        idx = 0
        res = ""
        for letter in s:
            if letter != "?":
                res += letter
            else:
                res += a[idx]
                idx+=1
        return res
