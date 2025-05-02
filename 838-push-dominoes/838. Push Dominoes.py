class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        L_indicies = []
        R_indicies = [] 
        res = [c for c in dominoes]
        for i, c in enumerate(dominoes):
            if c == "R":
                R_indicies.append(i)
            elif c == "L":
                L_indicies.append(i)
        if not R_indicies and not L_indicies:
            return dominoes
        elif not R_indicies:
            for i in range(L_indicies[-1]):
                res[i] = "L"
            return "".join(res)
        elif not L_indicies:
            for i in range(R_indicies[0], len(dominoes)):
                res[i] = "R"
            return "".join(res)

        # Case L and R intersect
        for a, idx in enumerate(L_indicies):
            # Check the cloest R_indicies to the left
            i=bisect_left(R_indicies, idx)
            if i == 0:
                # Case where L is leftmost
                for i in range(idx):
                    res[i] = "L"
            else:
                r_idx = R_indicies[i-1]
                print('reached', r_idx)
                if a == 0 or (idx > 0 and "R" in res[L_indicies[a-1] : idx]):
                    l, r = r_idx, idx
                    print(l, r)
                    while l < r:
                        res[l] = "R"
                        res[r] = "L"
                        l += 1
                        r -= 1

        idx = bisect_right(L_indicies, R_indicies[-1])
        if idx == len(L_indicies):
            for i in range(R_indicies[-1], len(dominoes)):
                res[i] = "R"
        print(res)
        for i in range(1, len(R_indicies)):
            s, e = R_indicies[i-1], R_indicies[i]
            if "L" not in res[s:e]:
                for i in range(s, e):
                    res[i] = "R"
        for i in range(1, len(L_indicies)):
            s, e = L_indicies[i-1], L_indicies[i]
            if "R" not in res[s:e]:
                for i in range(s, e):
                    res[i] = "L"
        return "".join(res)

        # Case where R is on rightmost