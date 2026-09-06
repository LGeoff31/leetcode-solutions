class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)

        if total_sum % 3 != 0:
            return False 
        
        target = total_sum // 3
        complete = 0
        curr = 0
        reached = False
        for i, n in enumerate(arr):
            if complete == 2:
                curr += sum(arr[i:])
                reached = True
                break 
        
            curr += n
            if curr == target:
                curr = 0
                complete += 1
        if reached and curr == target: 
            print('reached', curr)
            complete += 1
        return complete == 3