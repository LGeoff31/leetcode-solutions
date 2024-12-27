class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        negative = str(num)[0] == "-"
        a = bin(num)[2:]
        if negative:
            a = bin(int(str(num)[1:]))[2:]
        binary_rep = "0" * (32-len(a)) + a
        print(binary_rep)
        res = ""
        dic = {10:'a', 11:'b', 12:"c", 13:'d', 14:"e", 15:"f"}
        byte = 0
        if negative:
            rightmost_1 = binary_rep.rindex("1")
            idx = 0
            lst = list(binary_rep)
            while idx != rightmost_1:
                lst[idx] = "1" if lst[idx] == "0" else "0"
                idx += 1
            binary_rep = "".join(lst)
            
        for i in range(len(binary_rep) -1, -1, -4):
            # print(i, 2**(31-(i-1)),  2**(31-(i-3)))
            val = 0
            val += 2**(31-i) if binary_rep[i] == "1" else 0
            val += 2**(31-(i-1)) if binary_rep[i-1] == "1" else 0
            val += 2**(31-(i-2)) if binary_rep[i-2] == "1" else 0
            val += 2**(31-(i-3)) if binary_rep[i-3] == "1" else 0
            print(val)
            val //= 16**byte
            if val >= 0:
                if val < 10:
                    res += str(val)
                else:
                    res += dic[val]
            byte += 1
        res = res[::-1]
        print(res)
        for i in range(len(res)):
            if res[i] != "0":
                return res[i:]
        # return res[::-1]