class Solution:
    def solveEquation(self, equation: str) -> str:
        # Infinite solution when same number x's on both sides
        # No solution when same x's on both sides but constants different
        # Otherwise, single solution
        lhs, rhs = equation.split("=")
        def get_preceeding(idx, side):
            if idx == 0: return 1
            preceed = ""
            for i in range(idx - 1, -1, -1):
                if side[i] == "+":
                    if not preceed: return 1
                    return int(preceed[::-1])
                if side[i] == "-":
                    if not preceed: return -1
                    return -int(preceed[::-1])
                preceed += side[i]
            return int(preceed[::-1])
        def get_x_count(side):
            count = 0
            for i in range(len(side)):
                if side[i] == "x":
                    preceeding = get_preceeding(i, side) # -100, 2, 5, -1 (no preceeding)
                    count += preceeding
            return count
        def get_constants(side):
            res = []
            negative = False
            idx = 0
            while idx < len(side):
                if side[idx] == "-":
                    negative = True
                    if idx+1 < len(side) and side[idx+1] == "x":
                        negative = False
                if not side[idx].isdigit():
                    idx += 1
                    continue
                a = ""
                
                while idx < len(side) and side[idx].isdigit():
                    a += side[idx]
                    idx += 1
                if idx < len(side) and side[idx] == "x":
                    idx += 1
                    negative = False
                    continue
                if negative:
                    res.append(-int(a))
                    negative = False
                else:
                    res.append(int(a))
            return res
                    

        lhs_x = get_x_count(lhs)
        rhs_x = get_x_count(rhs)
        print(lhs_x)
        print(rhs_x)
        lhs_constants = sum(get_constants(lhs))
        rhs_constants = sum(get_constants(rhs))
        if lhs_x == rhs_x and lhs_constants != rhs_constants: return "No solution"
        if lhs_x == rhs_x: return "Infinite solutions"
        print(lhs_constants)
        print(rhs_constants)
        return f"x={str(int((rhs_constants-lhs_constants) / (lhs_x - rhs_x)))}"
