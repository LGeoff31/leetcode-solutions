class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = [i for i in range(1, len(s) + 2)]
        l = 0
        a = []
        while l < len(s):
            if s[l] == "D":
                r = l
                while r < len(s) and s[r] == "D":
                    r += 1
                # Reverse [l: r+1]
                temp_lst = res[l:r+1][::-1]
                # print(l, r, temp_lst, res)
                for i in range(l, r+1):
                    res[i] = temp_lst[i-l]
                    # print('replace', res[i], temp_lst[-((i-l)+1)])
                # print('res', res)
                l = r
            else:
                l += 1
            r = l

        return res