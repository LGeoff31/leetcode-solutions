class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        a_sum = sum(apple)
        c_pref = list(accumulate(capacity))
        print(c_pref)
        return bisect_left(c_pref, a_sum) + 1