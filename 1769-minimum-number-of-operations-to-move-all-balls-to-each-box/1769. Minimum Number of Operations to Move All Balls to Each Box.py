class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        right = [0] * n
        left = [0] * n
        for i in range(len(boxes) -2, -1, -1):
            if boxes[i+1] == "1":
                right[i] = 1 + right[i+1]
            else:
                right[i] = right[i+1]
        for i in range(1, len(boxes)):
            if boxes[i-1] == "1":
                left[i] = 1 + left[i-1]
            else:
                left[i] = left[i-1]
        prefixLeft = [0] * n
        prefixRight = [0] * n
        for i in range(1, n):
            prefixLeft[i] = prefixLeft[i-1] + left[i]
        for i in range(n-2, -1, -1):
            prefixRight[i] = prefixRight[i+1] + right[i]
        ans = []
        print(prefixRight)
        print(prefixLeft)
        for i in range(len(prefixRight)):
            ans.append(prefixRight[i] + prefixLeft[i])
        return ans
      