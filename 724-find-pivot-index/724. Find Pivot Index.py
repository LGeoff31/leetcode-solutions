class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        suffix = []
        acc = 0
        for num in nums:
            acc += num
            prefix.append(acc)
        acc = 0
        for num in nums[::-1]:
            acc += num
            suffix.append(acc)
        suffix = suffix[::-1]
        print(prefix)
        print(suffix)
        if len(nums) == 1:
            return 0

        for i in range(len(prefix)):
            if i == 0:
                if suffix[(i+1)] == 0:
                    return i
            elif i == len(prefix) - 1:
                if prefix[i-1] == 0:
                    return i
            elif prefix[i-1] == suffix[i+1]:
                return i
        return -1
        
        