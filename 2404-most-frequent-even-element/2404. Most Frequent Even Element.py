class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        lst = [(nums.count(num), num) for num in nums]
        # lst.sort(reverse=True)
        lst = sorted(lst, reverse=True)
        print(lst)
        freq = lst[0][0]
        for i in range(len(lst)):
            if lst[i][1]%2==0:
                freq = lst[i][0]
                break
        res = 1e9
        for i in range(len(lst)):
            if lst[i][1]%2==0 and lst[i][0] == freq:
                res = min(res, lst[i][1])
        return res if res != 1e9 else -1