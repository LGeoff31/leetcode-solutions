class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = Counter(word)
        # 26 alphabet, 2 -> 9: 8 numbers
        lst = []
        for key in dic:
            lst.append((dic[key], key))
        lst.sort(reverse=True)
        print(lst, len(lst))
        if len(lst) <= 8:
            return sum(a for a,b in lst)
        if len(lst) <= 16:
            return sum(a for a,b in lst[:8]) + 2*sum(a for a,b in lst[8:])
        if len(lst) <= 24:
            return sum(a for a,b in lst[:8]) + 2*sum(a for a,b in lst[8:16]) + 3*sum(a for a,b in lst[16:])
        else:
            return sum(a for a,b in lst[:8]) + 2*sum(a for a,b in lst[8:16]) + 3*sum(a for a,b in lst[16:24]) + 4*sum(a for a,b in lst[24:])