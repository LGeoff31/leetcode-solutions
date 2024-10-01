class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(arr)):
            val = arr[i] % k
            dic[val] = 1 + dic.get(val, 0)
        print(dic)
        visited = set()
        for key in dic:
            if key not in visited:
                complement = (k - key)%k
                if (complement not in dic and complement != 0) or dic[complement] != dic[key] or (complement in dic and complement == 0 and dic[complement] % 2 == 1):
                    return False 
                visited.add(key)
                visited.add(complement)
        return True