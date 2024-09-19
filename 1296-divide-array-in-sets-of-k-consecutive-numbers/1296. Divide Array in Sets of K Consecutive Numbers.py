class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False 
        nums.sort()
        dic = Counter(nums)
        print(nums)
        a = sorted(list(set(nums)))
        print('a', a)
        for i in range(len(a)):
            while a[i] in dic:
                for p in range(a[i], a[i] + k):
                    if p not in dic:
                        return False 
                    dic[p] -= 1
                    if dic[p] == 0:
                        del dic[p]
            # print(dic)
        return True