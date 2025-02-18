class Solution:
    def smallestNumber(self, pattern: str) -> str:
        length = len(pattern) + 1
        a = list(range(1,length+1))
        lst = list(permutations(a))
        # print(lst)
        def valid(arr):
            idx = 0
            for i in range(1, len(arr)):
                if pattern[idx] == "I":
                    if arr[i] < arr[i-1]:
                        return False
                else:
                    if arr[i] > arr[i-1]:
                        return False
                idx += 1
            return True 
        for arr in lst:
            if valid(arr):
                res = ""
                for c in arr:
                    res += str(c)
                return res
                # return "".join([c for c in arr])
        return ""