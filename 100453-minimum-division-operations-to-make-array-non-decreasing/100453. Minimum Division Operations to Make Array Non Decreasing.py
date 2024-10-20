class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def div(x): # O(sqrtn)
            divisors = []

            for i in range(1, int(x ** 0.5) + 1):
                if x % i == 0:
                    if i < x:
                        divisors.append(i)
                    if x // i < x and i != x // i: # No divide by 1 and itself and no double counting sqrt
                        divisors.append(x // i)
            if divisors:
                return max(divisors)
            return 1

        def is_prime(n):
            if n <= 1:
                return True
            if n == 2:
                return True  
            if n % 2 == 0:
                return False 

            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        res = 0

        # Make first num as small as possible
        # while not is_prime(nums[0]):
        #     lst = div(nums[0])
        #     if lst:
        #         nums[0] //= lst[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i+1]:
                while not is_prime(nums[i]) and nums[i] > nums[i+1]:
                    nums[i] = nums[i] // div(nums[i])
                    res += 1
                if nums[i] > nums[i+1]:
                    return -1

        return res