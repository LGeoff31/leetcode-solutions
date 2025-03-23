class Solution:
    def countNicePairs(self, arr: List[int]) -> int:
        res = 0
        differences = defaultdict(int) #O (n)
        MOD = 10 ** 9 + 7

        def rev(num): #O(log10(num))
            return int(str(num)[::-1])

        for i in range(len(arr)): # O(n)
            curr_diff = arr[i] - rev(arr[i])
            if curr_diff in differences:
                res += differences[curr_diff] 
            differences[curr_diff] += 1
            
        return res % MOD