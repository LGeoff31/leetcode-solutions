from collections import deque
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = deque([])
        negatives = deque([])
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        lst = []
        while positives and negatives:
            pos = positives.popleft()
            neg = negatives.popleft()
            lst.append(pos)
            lst.append(neg)
        return lst
