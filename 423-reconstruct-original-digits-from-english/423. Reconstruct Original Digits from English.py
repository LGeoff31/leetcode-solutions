class Solution:
    def originalDigits(self, s: str) -> str:
        dic = Counter(s)
        res = ""
        while "z" in dic and "e" in dic and "o" in dic and "r" in dic and dic["z"] > 0 and dic["e"] > 0 and dic["o"] > 0 and dic["r"] > 0:
            dic["z"] -= 1
            dic["e"] -= 1
            dic["o"] -= 1
            dic["r"] -= 1
            res += "0"

        while "w" in dic and "t" in dic and "o" in dic and dic["w"] > 0 and dic["t"] > 0 and dic["o"] > 0:
            dic["w"] -= 1
            dic["t"] -= 1
            dic["o"] -= 1
            res += "2"

        while "u" in dic and "f" in dic and "o" in dic and "r" in dic and dic["u"] > 0 and dic["f"] > 0 and dic["o"] > 0 and dic["r"] > 0:
            dic["u"] -= 1
            dic["f"] -= 1
            dic["o"] -= 1
            dic["r"] -= 1
            res += "4"

        while "x" in dic and "s" in dic and "i" in dic and dic["x"] > 0 and dic["s"] > 0 and dic["i"] > 0:
            dic["x"] -= 1
            dic["s"] -= 1
            dic["i"] -= 1
            res += "6"

        while "g" in dic and "e" in dic and "i" in dic and "h" in dic and "t" in dic and dic["g"] > 0 and dic["e"] > 0 and dic["i"] > 0 and dic["h"] > 0 and dic["t"] > 0:
            dic["g"] -= 1
            dic["e"] -= 1
            dic["i"] -= 1
            dic["h"] -= 1
            dic["t"] -= 1
            res += "8"

        while "h" in dic and "t" in dic and "r" in dic and "e" in dic and dic["h"] > 0 and dic["t"] > 0 and dic["r"] > 0 and dic["e"] > 1:
            dic["h"] -= 1
            dic["t"] -= 1
            dic["r"] -= 1
            dic["e"] -= 2
            res += "3"

        while "f" in dic and "i" in dic and "v" in dic and "e" in dic and dic["f"] > 0 and dic["i"] > 0 and dic["v"] > 0 and dic["e"] > 0:
            dic["f"] -= 1
            dic["i"] -= 1
            dic["v"] -= 1
            dic["e"] -= 1
            res += "5"

        while "s" in dic and "e" in dic and "v" in dic and "e" in dic and "n" in dic and dic["s"] > 0 and dic["e"] > 1 and dic["v"] > 0 and dic["n"] > 0:
            dic["s"] -= 1
            dic["e"] -= 2
            dic["v"] -= 1
            dic["n"] -= 1
            res += "7"

        while "o" in dic and "n" in dic and "e" in dic and dic["o"] > 0 and dic["n"] > 0 and dic["e"] > 0:
            dic["o"] -= 1
            dic["n"] -= 1
            dic["e"] -= 1
            res += "1"

        while "i" in dic and "n" in dic and "e" in dic and dic["i"] > 0 and dic["n"] > 1 and dic["e"] > 0:
            dic["i"] -= 1
            dic["n"] -= 2
            dic["e"] -= 1
            res += "9"

        return "".join(sorted(res))