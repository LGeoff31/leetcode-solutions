from sortedcontainers import SortedList
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        lst = SortedList()
        dic = {}
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] in dic:
                newNum = dic[nums[i]] + freq[i]
                lst.discard(dic[nums[i]])
                dic[nums[i]] += freq[i]
                # lst.discard(freq[i])
                lst.add(newNum)    
            else:
                dic[nums[i]] = freq[i]
                lst.add(freq[i])
            # print(lst)
            res[i]=lst[-1]
        return res
            
            
        