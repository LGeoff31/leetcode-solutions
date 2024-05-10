class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        dic = {}
        lst = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                dic[arr[i] / arr[j]] = [arr[i], arr[j]]
                lst.append(arr[i] / arr[j])
        lst.sort()
        return dic[lst[k-1]]
        