class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l, r = [0], [0]
        for n in nums[:-1]:
            l.append(l[-1] + n)
        for n in nums[::-1][:-1]:
            r.append(r[-1] + n)
        r=r[::-1]
        print(l, r)
        return list(abs(l[i] - r[i]) for i in range(len(l)))