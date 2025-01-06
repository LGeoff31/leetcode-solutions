class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            curr = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    curr += abs(j-i)
            ans.append(curr)
        return ans