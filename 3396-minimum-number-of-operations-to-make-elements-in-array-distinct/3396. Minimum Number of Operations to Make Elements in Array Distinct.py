class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dic = Counter(nums)
        count = 0
        size = len(nums)
        lst = deque(nums)
        while len(dic) != size:
            if size < 3:
                count += 1
                break 
            else:
                a = lst.popleft()
                b = lst.popleft()
                c = lst.popleft()
                dic[a] -= 1
                if dic[a] == 0: del dic[a]
                dic[b] -= 1
                if dic[b] == 0: del dic[b]
                dic[c] -= 1
                if dic[c] == 0: del dic[c]
                size -= 3
            count += 1

        return count