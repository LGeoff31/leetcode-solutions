class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime = []
        def is_prime(num):
            for i in range(2, floor(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        if len(nums) == 1: return True
        for i in range(2, 1001):
            if is_prime(i):
                prime.append(i)
        # for i in range(len(nums))
        tmp = nums[0]
        if bisect_left(prime, nums[0]) == 0:
            if i+1 < len(nums) and nums[i] >= nums[i+1]:
                    # print('reached')
                    return False
        else:
            if prime[bisect_left(prime, nums[0]) - 1] < nums[0]:
                nums[0] -= prime[bisect_left(prime, nums[0]) - 1]
            elif prime[bisect_left(prime, nums[0]) - 1] == nums[0]:
                nums[0] -=  prime[bisect_left(prime, nums[0]) - 1]
            else:
                return False
        if nums[0] < 0: nums[0] = tmp
        if nums[0] >= nums[1]: return False
        print('reached')
        for i in range(1, len(nums)):
            # print(nums)
            diff = nums[i] - nums[i-1]
            if bisect_left(prime, diff) == 0:
                if i+1 < len(nums) and nums[i] >= nums[i+1]:
                    # print('reached')
                    return False
                continue
            if prime[bisect_left(prime, diff) - 1] < nums[i]:
                nums[i] -= prime[bisect_left(prime, diff) - 1]
                # if nums[i]
            elif prime[bisect_left(prime, diff) - 1] == nums[i]:
                nums[i] -= prime[bisect_left(prime, diff) - 1]
            else:
                return False
            if i+1 < len(nums) and nums[i] >= nums[i+1]:
                return False
        return True