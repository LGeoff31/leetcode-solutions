class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Observations
        # Both are permutations of values [0, n-1]
        # For each array seperately, we can create a graph in O(n) that has a node pointing to next higher node using monotonic stack
        

        left, right = SortedList(), SortedList()
        indicies = []
        indicies_nums2 = {}
        for i, num in enumerate(nums2):
            indicies_nums2[num] = i
            right.add(num)
        for num in nums1:
            indicies.append(indicies_nums2[num])
        res = 0
        for num in indicies:
            right.remove(num)
            if not left:
                pass
            elif not right:
                continue
            else:
                elements_less_than_curr = bisect_left(left, num)
                elements_grea_than_curr = len(right) - bisect_left(right, num)
                res += elements_less_than_curr * elements_grea_than_curr
            left.add(num)
            print(res, num)
        return res