from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1, a2 = [nums[0]], [nums[1]]
        arr1 = SortedList([nums[0]])
        arr2 = SortedList([nums[1]])
        def greaterCount(arr, val):
            return len(arr) - arr.bisect_right(val)
            # #base cases
            # if val > arr[-1]: return 0
            # if val < arr[0]: return len(arr)

            # l, r = 0, len(arr) - 1

            # while l <= r: #[1,2,3,4,5], val = 2 -> 2
            #     mid = (l+r) // 2
            #     # print("mid", mid, arr[mid], arr[mid+1])
            #     if mid == len(arr) - 1:
            #         if arr[mid] > val and arr[mid-1] <= val: return 1
            #     elif arr[mid] <= val and arr[mid+1] > val:
            #         return len(arr) - (mid+1)
            #     elif arr[mid] > val:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # return -1

        for i in range(2, len(nums)): #O(n)
            a,b = greaterCount(arr1, nums[i]), greaterCount(arr2, nums[i]) #O(logn)
            print(nums[i], a, b)
            if a > b:
                arr1.add(nums[i])
                a1.append(nums[i])
            elif a < b:
                arr2.add(nums[i])
                a2.append(nums[i])
            else:
                if len(arr1) <= len(arr2):
                    arr1.add(nums[i])
                    a1.append(nums[i])
                else:
                    arr2.add(nums[i])
                    a2.append(nums[i])

        return a1 + a2


