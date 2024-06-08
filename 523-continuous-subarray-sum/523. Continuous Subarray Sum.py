class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        prefix = []
        acc = 0

        for i in range(len(nums)-1):
            if nums[i]==0 and nums[i+1] ==0:return True
            if nums[i] == 0 and nums[i+1] %k==0 or nums[i]%k==0 and nums[i+1]==0: return True
            # if nums[i]%k == 0: return True



        for num in nums:
            acc += num
            prefix.append(acc)

        dic={}
        print(prefix)
        for i in range(len(prefix)):
            if nums[i] != 0 and ((prefix[i] % k == 0 and i!=0) or (prefix[i] % k in dic and i - dic[prefix[i] % k]) > 1): 
                print(i)
                # print(visited)
                return True
            else: 
                dic[prefix[i]%k] = i
                # visited.add(prefix[i] % k)
        return False

        #[1,1]
        