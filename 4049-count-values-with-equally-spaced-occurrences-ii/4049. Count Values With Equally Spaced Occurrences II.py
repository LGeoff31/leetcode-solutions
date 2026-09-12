class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        def is_integer_special(num):
            indicies = num_to_indicies[num]
            if len(indicies) < 3:
                return False 
            
            diff = indicies[1] - indicies[0]
            for i in range(1, len(indicies)):
                if indicies[i] - indicies[i-1] != diff:
                    return False
            
            return True
            
        num_to_indicies = defaultdict(list)
        for i, n in enumerate(nums):
            num_to_indicies[n].append(i)
        

        res = 0
        for num in num_to_indicies:
            res += is_integer_special(num)
        return res
