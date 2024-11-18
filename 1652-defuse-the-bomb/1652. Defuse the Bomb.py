class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0] * len(code)
        res = []

        def compute(idx, reverse):
            ans = 0
            count = 0
            if not reverse:
                for i in range(idx+1, len(code)):
                    ans += code[i]
                    count += 1
                    if count == k or count == -k: break
                while count != k:
                    for i in range(len(code)):
                        ans += code[i]
                        count += 1
                        if count == k or count == -k: break
            else:
                for i in range(idx -1 , -1, -1):
                    ans += code[i]
                    count += 1
                    if count == k or count == -k: break
                while count != k and count != -k:
                    for i in range(len(code) -1, -1, -1):
                        ans += code[i]
                        count += 1
                        if count == k or count == -k: break
            return ans

        for i in range(len(code)):
            if k > 0:
                res.append(compute(i, False))
            else:
                res.append(compute(i, True))
            print(res)
        return res