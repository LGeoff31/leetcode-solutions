class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7: return False

        def evaluate(arr):
            prefix = list(accumulate(arr))
            totalSum = sum(arr)
            possible_values = set()
            for pivot in range(1, len(arr)-1):
                leftSum = prefix[pivot] - arr[pivot]
                rightSum = totalSum - prefix[pivot]
                if leftSum == rightSum:
                    possible_values.add(leftSum)
            if len(possible_values) > 0:
                return [True, possible_values]
            return [False, set()]
        def intersection(a,b):
            for key in a:
                if key in b:
                    return True
            return False
        for pivot in range(3, n - 3):
            leftArr = nums[:pivot]
            rightArr = nums[pivot+1:]
            a,b = evaluate(leftArr)
            c,d = evaluate(rightArr)
            # print(leftArr, rightArr, a,c,b,d)
            if a and c and intersection(b, d):
                return True
        return False