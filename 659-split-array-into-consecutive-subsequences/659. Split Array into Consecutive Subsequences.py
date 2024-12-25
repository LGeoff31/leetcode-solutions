class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        subsequences = defaultdict(int)

        for i in range(len(nums)):
            if dic[nums[i]] <= 0:
                continue
            
            if subsequences[nums[i]-1] > 0: # Attach on existing subsequence
                dic[nums[i]] -= 1
                subsequences[nums[i]] += 1
                subsequences[nums[i] - 1] -= 1

                continue
            elif dic[nums[i]+1] > 0 and dic[nums[i] + 2] > 0:
                subsequences[nums[i] + 2] += 1
                dic[nums[i] + 1] -= 1
                dic[nums[i] + 2] -= 1
            else:
                return False
            dic[nums[i]] -= 1
            print(dic, subsequences)
        return True



