class Solution:
    def maximumSwap(self, num: int) -> int:
        a = str(num)
        idx = 0
        while idx < len(a):
            max_idx = -1
            max_num = -1e9
            for i in range(len(a)-1, idx, -1):
                if int(a[i]) > max_num:
                    max_num = int(a[i])
                    max_idx = i
            lst = [ch for ch in a]
            if lst[max_idx] > lst[idx]:
                lst[max_idx], lst[idx] = lst[idx], lst[max_idx]
                back = "".join(lst)
                return int(back)
            idx += 1
                
        return int(num)