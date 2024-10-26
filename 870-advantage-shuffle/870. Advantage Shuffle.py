from sortedcontainers import SortedList
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp_nums2 = nums2.copy()
        lst1 = SortedList(nums1)
        lst2 = SortedList(nums2)

        dic = defaultdict(list)
        for num in lst1:
            # Pair each num to be greater than one in nums2, otherwise pair with largest in nums2
            idx = bisect.bisect_left(lst2, num)

            if idx == 0 or idx >= len(lst2):
                # Pair it with the largest value
                dic[lst2[-1]].append(num)
                lst2.remove(lst2[-1])
            else:
                # Find index pair it with
                dic[lst2[idx - 1]].append(num)
                lst2.remove(lst2[idx - 1])

        res = []
        for i in range(len(temp_nums2)):
            res.append(dic[temp_nums2[i]][-1])
            lst = dic[temp_nums2[i]]
            lst.pop()
            # if dic[temp_nums2[i]]: dic[temp_nums2[i]].pop()
        
        print(dic)

        return res
            

