class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # product remaining elements % k = x
        # suffix and prefix can me empty themselves
        # O(n), note k is very small so take advantage of this
        
        # Nicer to work with (product - i) % k == 0
        # Store in hashmap?
        res = [0] * k
        dic = {}

        for i in range(len(nums)):
            temp = defaultdict(int)
            val = nums[i] % k
            temp[val] += 1

            for key in dic:
                new_val = (nums[i] * key) % k
                temp[new_val] += dic[key]

            for key in temp:
                res[key] += temp[key]
            dic = temp
        return res